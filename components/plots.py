import plotly.express as px


def plot_line(data, X, Y, C, S):
    try:
        fig = px.line(data, X, Y, color=C)
    except:
        fig = plot_error()
    return fig


def plot_scatter(data, X, Y, C, S):
    try:
        fig = px.scatter(data, X, Y, color=C, size=S)
    except:
        fig = plot_error()
    return fig


def plot_hist(data, X, Y, C, S):
    try:
        fig = px.histogram(data, X, Y, color=C, pattern_shape=S)
    except:
        fig = plot_error()
    return fig


def plot_dist(data, X, Y, C, S):
    try:
        fig = px.density_contour(data, X, Y, color=C)
    except:
        fig = plot_error()
    return fig


def plot_corr(data, X, Y, C, S):
    if X == None:
        try:
            corr_data = data.corr().round(2)
            fig = px.imshow(corr_data, text_auto=True)
        except:
            fig = plot_error()
    else:
        try:
            corr_data = data.corr().round(2)
            corr_data = corr_data[[X]].T
            fig = px.imshow(corr_data, text_auto=True)
        except:
            fig = plot_error()
    return fig


def plot_pie(data, X, Y, C, S):
    try:
        fig = px.pie(data, values=Y, names=X, color=C)
    except:
        fig = plot_error()
    return fig


def plot_bar(data, X, Y, C, S):
    try:
        fig = px.bar(data, X, Y, color=C, pattern_shape=S)
    except:
        fig = plot_error()
    return fig


def plot_violin(data, X, Y, C, S):
    try:
        fig = px.violin(data, X, Y, color=C)
    except:
        fig = plot_error()
    return fig


def plot_box(data, X, Y, C, S):
    try:
        fig = px.box(data, X, Y, color=C)
    except:
        fig = plot_error()
    return fig


def plot_count(data, X, Y, C, S):
    try:
        fig = px.density_heatmap(data, X, Y, text_auto=True)
    except:
        fig = plot_error()
    return fig


def plot_error():
    fig = px.scatter(
        x=[0], y=[0], text=["Error"], range_x=[-0.1, 0.1], range_y=[-0.1, 0.1]
    )
    fig.update_layout(font=dict(size=70))
    return fig
