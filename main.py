import pandas as pd
import kagglehub
import seaborn as sns
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("aminealibi/ufc-fights-fighters-and-events-dataset")
print("Path to dataset files:", path)

# 2. Create the DataFrame (for example, from a CSV file)
df1 = pd.read_csv( path + '\\raw_data\\raw_fights.csv')  # Ensure the file path is correct (in this case windows file so \\ were needed)

df2 = pd.read_csv( path + '\\raw_data\\raw_events.csv')  # Ensure the file path is correct
df = pd.merge(df1, df2, on=['Event_Id','Event_Id'])
# 3. Now you can use it
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# Get weight class counts and calculate percentages
weight_class_counts = df['Weight_Class'].value_counts()
total_fights = len(df)
percentages = (weight_class_counts / total_fights * 100).round(1)

# Group smaller categories into "Other" if there are too many
if len(weight_class_counts) > 10:
    threshold = weight_class_counts.iloc[9]  # 10th largest count
    main_classes = weight_class_counts[weight_class_counts >= threshold]
    other_count = weight_class_counts[weight_class_counts < threshold].sum()
    other_percentage = (other_count / total_fights * 100).round(1)
    
    # Create new series with "Other" category
    pie_data = main_classes.copy()
    pie_percentages = percentages[main_classes.index]
    # if other_count > 0:
    #     pie_data['Other'] = other_count
    #     pie_percentages = pd.concat([pie_percentages, pd.Series([other_percentage], index=['Other'])])
else:
    pie_data = weight_class_counts
    pie_percentages = percentages

# Create the pie chart without percentages on slices
colors = sns.color_palette('Set3', len(pie_data))
wedges, labels = plt.pie(pie_data.values, 
                        colors=colors,
                        startangle=90)

# Create custom legend labels with percentages
legend_labels = [f'{label}: {pie_percentages[label]}% ({pie_data[label]} fights)' 
                for label in pie_data.index]

plt.legend(wedges, legend_labels,
          title="Weight Classes",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10)

plt.title('Distribution of UFC Fights by Weight Class\n', fontsize=16, fontweight='bold')
plt.axis('equal')

plt.tight_layout()
plt.show()

# Print summary statistics
print("="*60)
print("WEIGHT CLASS DISTRIBUTION SUMMARY")
print("="*60)
print(f"Total fights in dataset: {len(df):,}")
print(f"Number of unique weight classes: {len(weight_class_counts)}")
