import plotly.express as px


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
        color_discrete_sequence=px.colors.qualitative.Pastel2_r,
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
        color_discrete_sequence=px.colors.qualitative.Pastel2_r,
        hole=0.5,
        width=250,
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
