#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[9]:


import pandas as pd


#load the dataset

df = pd.read_csv("C:/Users/shrey/OneDrive/Desktop/project/DataScience_salaries_2024.csv")


# In[20]:


print(df.head())


# In[27]:


df


# In[10]:


summary_statistics= df.describe()
df.describe()


# In[21]:


data_types_missing= df.info()
#there are no null values in the dataset


# In[8]:


print(df.nunique())


# In[12]:


#transformation of the codes of the categoricl variables
df['experience_level'] = df['experience_level'].replace({'SE': 'Expert', 'MI': 'Intermediate', 'EN': 'Junior', 'EX': 'Director'})

df['employment_type'] = df['employment_type'].replace({'FT': 'Full-time', 'CT': 'Contract', 'FL': 'Freelance', 'PT': 'Part-time'})

def country_name(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except:
        return 'other'
    
df['company_location'] = df['company_location'].apply(country_name)
df['employee_residence'] = df['employee_residence'].apply(country_name)


# In[13]:


# Categorical variables

for column in ['work_year','experience_level','employment_type','company_size','remote_ratio','job_title','company_location']:
    print(df[column].unique())


# In[15]:


import matplotlib.pyplot as plt
import seaborn as sns

# Extract the "job title" column
job_titles = df['job_title']

# Calculate the frequency of each job title
title_counts = job_titles.value_counts()

# Extract the top 20 most frequent job titles
top_20_titles = title_counts.head(20)

# Create a DataFrame for the top 20 titles
top_20_df = pd.DataFrame({'Job Title': top_20_titles.index, 'Count': top_20_titles.values})

# Plotting the count plot
plt.figure(figsize=(12, 6))
sns.set(style="darkgrid")
ax = sns.barplot(data=top_20_df, x='Count', y='Job Title', palette='cubehelix')
plt.xlabel('Count')
plt.ylabel('Job Titles')
plt.title('Top 20 Most Frequent Job Titles')

# Add count labels to the bars
for i, v in enumerate(top_20_df['Count']):
    ax.text(v + 0.2, i, str(v), color='black', va='center')

plt.tight_layout()
plt.show()


# In[16]:


#calculate the number of individuals in each experience level
level_counts = df['experience_level'].value_counts()

# Create a pie chart
plt.figure(figsize=(7,12),dpi=80)
plt.pie(level_counts.values, labels=level_counts.index, autopct='%1.1f%%')
plt.title('Experience Level Distribution')

plt.show()


# In[19]:


# Create a cross-tabulation of the two columns
cross_tab = pd.crosstab(df['experience_level'], df['company_size'])

# Create a heatmap using the cross-tabulation data
plt.figure(figsize=(10, 8))
sns.heatmap(cross_tab, annot=True, fmt="d", cmap='Reds')

plt.xlabel('Company Size')
plt.ylabel('Experience Level')
plt.title('Relationship between Experience Level and Company Size')

plt.show()


# In[22]:


import matplotlib.pyplot as plt
from matplotlib import ticker
# Create bar chart
average_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
top_ten_salaries = average_salary.head(10)

plt.figure(figsize=(15,10),dpi=80)
plt.bar(top_ten_salaries.index, top_ten_salaries)

# Add labels to the chart
plt.xlabel('Job')
plt.ylabel('Salary $')
plt.title('Average of the ten highest salaries by Job Titles')
plt.xticks(rotation=35, ha='right')
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()


# In[25]:


import plotly.express as px
salary_by_country = df.groupby('company_location', as_index=False)['salary_in_usd'].mean()

fig = px.choropleth(salary_by_country,locations='company_location',locationmode='country names',color='salary_in_usd',
                    projection='equirectangular',hover_name='company_location',
                    labels={'salary_in_usd':'Average Salary in USD'},title='Distribution of average salary by company location')


fig.show("notebook")


# In[33]:


common_jobs = ['Data Engineer', 'Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Analytics Engineer','Research Scientist', 'Data Science Manager', 'Applied Scientist']
common_jobs = df[df['job_title'].isin(common_jobs)]


# In[35]:


salary_common_jobs = common_jobs.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
remote_common_jobs = common_jobs.groupby('job_title')['remote_ratio'].mean().sort_values(ascending=False)
salary_common_country = common_jobs.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)


# In[36]:


# Create bar chart
salary_common_jobs = common_jobs.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

plt.figure(figsize=(15,10),dpi=80)
plt.bar(salary_common_jobs.index, salary_common_jobs)

# Add labels to the chart
plt.xlabel('Job')
plt.ylabel('Salary $')
plt.title('Average salary for common Job Titles')
plt.xticks(rotation=20, ha='right')
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()


# In[37]:


# Create bar chart
remote_common_jobs = common_jobs.groupby('job_title')['remote_ratio'].mean().sort_values(ascending=False)

plt.figure(figsize=(15,10),dpi=80)
plt.bar(remote_common_jobs.index, remote_common_jobs)

# Add labels to the chart
plt.xlabel('Job')
plt.ylabel('% remote')
plt.title('Remote rate by Job Titles')
plt.xticks(rotation=20, ha='right')
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()


# In[17]:


# Distribution of experience_level
print(df['experience_level'].value_counts())

# Distribution of employment_type
print(df['employment_type'].value_counts())

# Distribution of company_size
print(df['company_size'].value_counts())


# In[18]:


# Average salary by experience level
print(df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False))


# In[13]:


pip install matplotlib seaborn


# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting average salary by experience level
plt.figure(figsize=(10, 6))
sns.barplot(x=df['experience_level'], y=df['salary_in_usd'], estimator=np.mean)
plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')
plt.title('Average Salary by Experience Level')
plt.show()


# In[17]:


# Correlation matrix
correlation_matrix = df.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[18]:


# Bar chart for average salary by experience level
plt.figure(figsize=(10, 6))
sns.barplot(x='experience_level', y='salary_in_usd', data=df, estimator=np.mean, ci=None)
plt.title('Average Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')
plt.show()


# In[ ]:




