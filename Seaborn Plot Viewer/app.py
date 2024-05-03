import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets names
dataset_names = sns.get_dataset_names()

# Sidebar for user inputs
st.sidebar.header('User Input Features')
selected_dataset = st.sidebar.selectbox('Select a dataset', dataset_names)

# Load the selected dataset
data = sns.load_dataset(selected_dataset)

# Select plot
plot_types = ['scatterplot', 'lineplot', 'histplot', 'boxplot', 'violinplot',
              'barplot', 'countplot', 'pairplot', 'heatmap', 'jointplot', 'kdeplot']
plot_type = st.sidebar.selectbox('Select the type of plot', plot_types)

# Options for different plots
if plot_type in ['scatterplot', 'lineplot', 'barplot', 'countplot']:
    x_var = st.sidebar.selectbox('Choose X variable', data.columns)
    y_var = st.sidebar.selectbox('Choose Y variable', data.columns if plot_type != 'countplot' else ['None'])
    hue_var = st.sidebar.selectbox('Hue (optional)', ['None'] + list(data.columns), index=0)
elif plot_type in ['histplot', 'boxplot', 'violinplot', 'kdeplot']:
    x_var = st.sidebar.selectbox('Choose variable', data.columns)
    hue_var = st.sidebar.selectbox('Hue (optional)', ['None'] + list(data.columns), index=0)
elif plot_type == 'jointplot':
    x_var = st.sidebar.selectbox('Choose X variable', data.columns)
    y_var = st.sidebar.selectbox('Choose Y variable', data.columns)
elif plot_type == 'pairplot':
    hue_var = st.sidebar.selectbox('Hue (optional for pairplot)', ['None'] + list(data.columns), index=0)
elif plot_type == 'heatmap':
    # Typically used for correlation matrices or pivot tables
    st.write("Heatmap will display correlation matrix for numerical data.")

# Handle hue
hue = None if hue_var == 'None' else hue_var

# Main area
st.title('Seaborn Plot Viewer')

# Generate plot based on the type
fig, ax = plt.subplots()

if plot_type == 'scatterplot':
    sns.scatterplot(data=data, x=x_var, y=y_var, hue=hue, ax=ax)
elif plot_type == 'lineplot':
    sns.lineplot(data=data, x=x_var, y=y_var, hue=hue, ax=ax)
elif plot_type == 'histplot':
    sns.histplot(data=data, x=x_var, hue=hue, ax=ax)
elif plot_type == 'boxplot':
    sns.boxplot(data=data, x=x_var, hue=hue, ax=ax)
elif plot_type == 'violinplot':
    sns.violinplot(data=data, x=x_var, hue=hue, ax=ax)
elif plot_type == 'barplot':
    sns.barplot(data=data, x=x_var, y=y_var, hue=hue, ax=ax)
elif plot_type == 'countplot':
    sns.countplot(data=data, x=x_var, hue=hue, ax=ax)
elif plot_type == 'pairplot':
    if hue:
        sns.pairplot(data=data, hue=hue)
    else:
        sns.pairplot(data=data)
    st.pyplot()
    st.stop()
elif plot_type == 'heatmap':
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
elif plot_type == 'jointplot':
    sns.jointplot(data=data, x=x_var, y=y_var, kind='scatter')
    st.pyplot()
    st.stop()
elif plot_type == 'kdeplot':
    sns.kdeplot(data=data, x=x_var, hue=hue, ax=ax)

st.pyplot(fig)
