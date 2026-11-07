"""Visual investigation dashboard using generated demonstration data."""
import networkx as nx
import plotly.graph_objects as go
import streamlit as st

from sentinelgraph.core import analyze_events, build_graph, generate_events

st.set_page_config(page_title="SentinelGraph AI", page_icon="🛡️", layout="wide")
st.markdown("""<style>
.stApp {background: #080f21; color: #e9efff;}
[data-testid="stMetric"] {background:#131e39;border:1px solid #283b63;padding:18px;border-radius:14px;}
h1,h2,h3 {color:#eaf2ff!important;}
</style>""", unsafe_allow_html=True)
st.title("🛡️ SentinelGraph AI")
st.caption("Security operations explorer | Synthetic data only | Rule-based illustrative scoring")
count = st.sidebar.slider("Events to generate", 100, 2000, 600, step=100)
threshold = st.sidebar.slider("Minimum risk score", 0, 100, 25, step=5)
st.sidebar.info("All users, devices, IP addresses and events are synthetic. Scores are not calibrated probabilities.")
frame = analyze_events(generate_events(count))
alerts = frame[frame.score >= threshold]
a, b, c, d = st.columns(4)
a.metric("Security events", len(frame))
b.metric("Flagged events", len(alerts))
c.metric("High / critical", int(frame.severity.isin(["high", "critical"]).sum()))
d.metric("Distinct users", frame.user.nunique())
st.subheader("Threat activity")
chart = frame.groupby("severity").size().reindex(["low", "medium", "high", "critical"], fill_value=0)
st.bar_chart(chart)
left, right = st.columns([1.3, 1])
with left:
    st.subheader("Investigation queue")
    st.dataframe(alerts[["event_id", "timestamp", "user", "device", "score", "severity"]],
                 use_container_width=True, hide_index=True)
with right:
    st.subheader("Explain an alert")
    selected = st.selectbox("Select event", frame.event_id.tolist())
    row = frame.loc[frame.event_id == selected].iloc[0]
    st.metric("Illustrative risk score", f"{row['score']}/100")
    st.write("**Severity:**", row["severity"].upper())
    if row["reasons"]:
        for reason in row["reasons"]:
            st.write("•", reason)
    else:
        st.write("No detection rules triggered.")
st.subheader("Entity relationship explorer")
st.caption("Graph connects an event to its synthetic user, device, and IP address.")
subset = frame.loc[frame.event_id == selected]
graph = build_graph(subset)
pos = nx.spring_layout(graph, seed=7)
edge_x, edge_y = [], []
for src, dst in graph.edges():
    x0, y0 = pos[src]
    x1, y1 = pos[dst]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
fig = go.Figure()
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines", line=dict(color="#476baf", width=2), hoverinfo="skip"))
fig.add_trace(go.Scatter(x=[pos[n][0] for n in graph.nodes()], y=[pos[n][1] for n in graph.nodes()],
                         text=list(graph.nodes()), mode="markers+text", textposition="top center",
                         marker=dict(size=22, color=["#ff527e" if n.startswith("event:") else "#34c5ff" for n in graph.nodes()]),
                         textfont=dict(color="#e5edff")))
fig.update_layout(paper_bgcolor="#101a31", plot_bgcolor="#101a31", font_color="#eaf2ff",
                  showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False), height=420,
                  margin=dict(l=20, r=20, t=40, b=20))
st.plotly_chart(fig, use_container_width=True)
st.download_button("Export filtered alerts (CSV)", alerts.to_csv(index=False).encode(),
                   file_name="sentinelgraph-alerts.csv", mime="text/csv")
st.caption("Prototype for education and portfolio use. Not a production SIEM or an autonomous AI agent.")
