import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")

st.title("Tips Dataset Visualization App")
st.write("This is a simple app to visualize the Tips dataset using Seaborn.")

# Helper function for Axes-level plots
def display_plot(title, plot_func):
    st.subheader(title)
    fig, ax = plt.subplots(figsize=(8, 6))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)

# --- Axes-level plots ---
def scatter_plot(ax):
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", size="size", palette="deep", ax=ax)
    ax.set_title("Scatter Plot of Total Bill vs Tip")

def line_plot(ax):
    sns.lineplot(data=tips, x="size", y="total_bill", hue="sex", marker="o", ax=ax)
    ax.set_title("Line Plot of Total Bill by Size and Gender")

def bar_plot(ax):
    sns.barplot(data=tips, x="day", y="total_bill", hue="sex", palette="muted", ax=ax)
    ax.set_title("Bar Plot of Total Bill by Day")

def box_plot(ax):
    sns.boxplot(data=tips, x="day", y="tip", hue="smoker", palette="Set2", ax=ax)
    ax.set_title("Box Plot of Tips by Day and Smoker Status")

def violin_plot(ax):
    sns.violinplot(data=tips, x="day", y="total_bill", hue="time", split=True, palette="pastel", ax=ax)
    ax.set_title("Violin Plot of Total Bill by Day and Time")

def count_plot(ax):
    sns.countplot(data=tips, x="day", hue="smoker", palette="dark", ax=ax)
    ax.set_title("Count Plot of Days by Smoker Status")

def reg_plot(ax):
    sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={'s':50}, line_kws={'color':'red'}, ax=ax)
    ax.set_title("Regression Plot of Total Bill vs Tip")

def hist_plot(ax):
    sns.histplot(data=tips, x="total_bill", bins=20, kde=True, color="blue", ax=ax)
    ax.set_title("Histogram of Total Bill with KDE")

def strip_plot(ax):
    sns.stripplot(data=tips, x="day", y="tip", hue="sex", jitter=True, palette="Set1", ax=ax)
    ax.set_title("Strip Plot: Tips by Day and Gender")

def kde_plot(ax):
    sns.kdeplot(data=tips, x="total_bill", hue="sex", fill=True, palette="tab10", ax=ax)
    ax.set_title("KDE Plot: Total Bill Density by Gender")

# --- Figure-level plots (need their own logic) ---
def pair_plot():
    st.subheader("Pair Plot")
    g = sns.pairplot(tips, hue="sex", vars=["total_bill", "tip", "size"], palette="husl")
    g.fig.suptitle("Pair Plot: Numeric Variables by Gender", y=1.02)
    st.pyplot(g.fig)

def cat_plot():
    st.subheader("Cat Plot (Point)")
    g = sns.catplot(data=tips, x="day", y="tip", hue="sex", kind="point", palette="bright")
    g.fig.suptitle("Catplot (Point): Tips by Day and Gender")
    st.pyplot(g.fig)

def joint_plot():
    st.subheader("Joint Plot")
    g = sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", hue="smoker", palette="coolwarm")
    g.fig.suptitle("JointPlot: Total Bill vs Tip", y=1.02)
    st.pyplot(g.fig)

def facet_grid():
    st.subheader("Facet Grid")
    g = sns.FacetGrid(tips, col="time", row="smoker", margin_titles=True)
    g.map(sns.histplot, "total_bill", bins=20, kde=True).add_legend()
    st.pyplot(g.fig)

# --- Display all plots ---
display_plot("Scatter Plot", scatter_plot)
display_plot("Line Plot", line_plot)
display_plot("Bar Plot", bar_plot)
display_plot("Box Plot", box_plot)
display_plot("Violin Plot", violin_plot)
display_plot("Count Plot", count_plot)
display_plot("Regression Plot", reg_plot)
display_plot("Histogram Plot", hist_plot)
display_plot("Strip Plot", strip_plot)
display_plot("KDE Plot", kde_plot)

pair_plot()
cat_plot()
joint_plot()
facet_grid()
