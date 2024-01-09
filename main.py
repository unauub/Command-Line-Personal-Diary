# Entry Creation: user can add entries to their diary. Each entry should include a title, date, and the actual content.

# Entry Listing: list all diary with their titles and dates.

#Search and Filter: search based on keywords or filter entries based on date ranges.

# Save and Load

  import os
  import datetime

  class personal_diary:
    def __init__(self, title, date, content):
      self.title = title
      self.date = date
      self.content = content


  def add_diary(diary, title, date, content):
    #diary is a list we'll be created in next lines
    entry = personal_diary(title, date, content)
    diary.append(entry)
    print("Entry added successfully!")

  def list_diary(diary):
    if not diary:
      print("No entries found.")

    else:
      for i, entry in enumerate(diary, start=1):
        print(f"{i}. {entry.title} ({entry.date})")
        print(entry.content)
        print()

  def search_diary(diary, keyword):
    results = [entry for entry in diary if keyword.lower() in entry.content.lower()]

    if not results:
      print("No matching entries found.")

    else:
      print(f"Matching entries for '{keyword}':")
      for i, entry in enumerate(results, 1):
          print(f"{i}. {entry.title} ({entry.date})")
          print(entry.content)
          print()

  def save_diary(diary, filename="diary.txt"):
    with open(filename, "w") as file:
        for entry in diary:
            file.write(f"{entry.title}\n{entry.date}\n{entry.content}\n---\n")

  def load_diary(filename="diary.txt"):
    diary = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                title = lines[i].strip()
                date = lines[i + 1].strip()
                content = lines[i + 2].strip()
                entry = personal_diary(title, date, content)
                diary.append(entry)
                i += 4  # Skip "---" separator
    return diary

  def main():
    diary = load_diary()

    while True:
        print("\n1. Add Entry\n2. List Entries\n3. Search Entries\n4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            date = input("Enter date (YYYY-MM-DD): ")
            content = input("Enter content: ")
            add_diary(diary, title, date, content)

        elif choice == '2':
            list_diary(diary)

        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            search_diary(diary, keyword)

        elif choice == '4':
            save_diary(diary)
            print("Diary saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

  if __name__ == "__main__":
    main()