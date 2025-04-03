import plotly.express as px
import numpy as np


COLOR_PALLET = px.colors.qualitative.Bold


def add_tilte(fig, title):
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=15, family="Arial", color="#2a4978"),
        )
    )
    return fig


def add_horizontal_legend(fig):
    fig.update_layout(
        legend=dict(
            orientation="h",
            title=None,
            y=1,
            x=1,
            xanchor="right",
            yanchor="bottom",
        ),
        legend_bordercolor="black",
        legend_borderwidth=1,
    )
    return fig


def create_gender_distribution_plot(df, field):
    fig = px.bar(
        df,
        x="geo",
        y="value",
        color="gender",
        barmode="group",
        log_y=True,
        template="plotly_white",
        color_discrete_sequence=COLOR_PALLET,
    )
    fig.update_layout(xaxis={"categoryorder": "total descending"})
    fig.update_layout(
        xaxis_tickangle=-30,
        xaxis=dict(
            categoryorder="total descending",
            tickangle=-30,
            title="<b>Administrative Units</b>",
            tickfont=dict(size=12),
            title_font=dict(size=12),
        ),
        yaxis=dict(
            title="<b>Number of People (Log Scale)</b>",
            tickfont=dict(size=12),
            title_font=dict(size=12),
            showgrid=True,
            gridcolor="rgba(200, 200, 200, 0.3)",
        ),
        height=600,
        margin=dict(l=0, r=25, t=0, b=0),
    )
    fig.update_traces(
        textfont_size=10,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        texttemplate="%{y:.2s}",
        hovertemplate="<b>Region:</b> %{x}<br>" "<b>Count:</b> %{y}<extra></extra>",
    )

    fig = add_horizontal_legend(fig)
    # fig = add_tilte(fig, f"<b>Gender Composition of  {field} Across Units</b>")
    return fig


def create_gender_distribution_pie(df, field):
    fig = px.pie(
        df,
        values="value",
        names="gender",
        color_discrete_sequence=COLOR_PALLET,
        hole=0.5,
        width=350,
    )

    # fig.update_layout(legend=dict(orientation="v"))
    fig = add_horizontal_legend(fig)
    fig.update_traces(
        textposition="inside", textinfo="percent+label", insidetextfont=dict(size=12)
    )

    fig.update_layout(
        uniformtext_minsize=12,
        uniformtext_mode="hide",
        margin=dict(l=10, r=10, t=10, b=10),
    )

    return fig


def create_tree_map(df):
    midpoint = np.median(df["value"])

    fig = px.treemap(
        df,
        path=[px.Constant("Canada"), "geo", "occupation_c", "education_filtered"],
        values="value",
        color="occupation_c",
        color_discrete_sequence=COLOR_PALLET,
        color_continuous_midpoint=midpoint,
        height=750,
        template="plotly_white",
    )

    fig.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        hoverlabel=dict(bgcolor="white", font_size=14, font_family="Helvetica"),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    fig.update_traces(
        root_color="lightgrey",
        textinfo="label+value+percent parent",
        texttemplate="<b>%{label}</b><br>(%{percentParent:.1%})",
        textposition="middle left",
        marker=dict(line=dict(width=0.5, color="black")),
        hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>%{percentParent:.1%} of parent<extra></extra>",
        textfont_size=15,
    )

    return fig


def create_polar_essentails(df):
    fig = px.line_polar(
        df,
        r="value",
        theta="occupation_c",
        color="geo",
        color_discrete_sequence=COLOR_PALLET,
        template="plotly_white",
        labels={"value": "Count (log)", "occupation_c": "Occupation Category"},
        hover_name="geo",
        hover_data={"value": ":.2f"},
        log_r=True,
        start_angle=30,
        line_close=True,
        line_shape="spline",
    )

    fig.update_layout(
        title=dict(
            font=dict(size=22, family="Arial", color="#2a4978"),
            x=0.5,
            xanchor="center",
        ),
        font=dict(family="Arial", size=13, color="#333"),
        polar=dict(
            radialaxis=dict(
                angle=45,
                showline=True,
                linewidth=2,
                gridcolor="rgba(10,10,10,0.2)",
                tickangle=0,
            ),
            angularaxis=dict(
                linewidth=2,
                gridcolor="rgba(10,10,10,0.2)",
                tickfont=dict(size=12),
            ),
        ),
        legend=dict(
            orientation="h",
            title=None,
            y=-0.45,
            x=0.5,
            xanchor="center",
            yanchor="bottom",
            bordercolor="black",
            borderwidth=1,
            font=dict(size=12),
        ),
        margin=dict(l=0, r=0, t=20, b=50),
    )

    return fig


def create_essentials_pie(df):
    fig = px.pie(
        df,
        values="value",
        names="geo",
        color_discrete_sequence=COLOR_PALLET,
        hole=0.5,
        labels={"value": "Count"},
        template="plotly_white",
    )

    fig.update_layout(
        font_family="Helvetica Neue",
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=True,
        legend_title_text="Regions",
        legend_font_size=12,
        legend_title_font_size=14,
    )

    # fig = add_horizontal_legend(fig)

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        insidetextfont=dict(color="black", size=14, family="Arial"),
        marker=dict(line=dict(color="white", width=2)),
        hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>",
        pull=[0.1 if i == df["value"].idxmax() else 0.02 for i in range(len(df))],
    )

    fig.update_layout(
        legend=dict(
            orientation="v",
        ),
        legend_bordercolor="black",
        legend_borderwidth=1,
        margin=dict(l=10, r=0, t=20, b=50),
    )

    return fig


def create_pie_chart(df, title: str = "Occupation Distribution"):

    # Create figure
    fig = px.pie(
        df,
        names="occupation_c",
        values="value",
        hole=0.75,
        color_discrete_sequence=COLOR_PALLET,
    )

    # Configure layout
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=True,
        legend=dict(
            font=dict(size=10),
            orientation="v",
            xanchor="left",
        ),
        legend_bordercolor="black",
        legend_borderwidth=1,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial"),
    )

    # Configure traces
    text_info = "percent+label"
    fig.update_traces(
        textposition="none",
        textinfo=text_info,
        hovertemplate="<b>%{label}</b><br>Value: %{value:,}<br>Percentage: %{percent}<extra></extra>",
        textfont=dict(size=12),
        marker=dict(line=dict(color="#FFFFFF", width=1)),
    )

    return fig
