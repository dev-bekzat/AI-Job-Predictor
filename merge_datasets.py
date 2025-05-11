import pandas as pd

# загруажем эти 2 файла
main_df = pd.read_csv("filtered_dataset.csv")
custom_df = pd.read_csv("my_custom_data.csv")

# чистим пустые колонки
main_df = main_df[['skills', 'Job Title']].dropna()
custom_df = custom_df[['skills', 'Job Title']].dropna()

# мерджим (объединяем)
merged_df = pd.concat([main_df, custom_df], ignore_index=True)

# сохраняем
merged_df.to_csv("combined_dataset.csv", index=False)

print("✅ Объединённый датасет сохранён как 'combined_dataset.csv'")