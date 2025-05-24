from pathlib import Path
numbering = input("何番目のABCか入力してください")
folder_path = Path("ABC" + numbering)
folder_path.mkdir()
file_names = ["A", "B", "C", "D", "E"]
for name in file_names:
    file_path = folder_path / (numbering + name + ".py")
    file_path.touch()
print("ABC準備完了")