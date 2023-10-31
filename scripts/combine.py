import glob
import os

filename = "../Driver.java"

os.makedirs(os.path.dirname(filename), exist_ok=True)

read_files = glob.glob("../src/*.java")

with open(filename, "wb") as outfile:
    code_lines = []
    import_lines = []

    for f in read_files:
        with open(f, "rb") as infile:
            code_lines.append(("//AUTOGENERATED FROM " + infile.name + "\n").encode())
            for line in infile:
                line = str(line, 'UTF-8')
                line = line.replace("public class", "class")
                line = line.replace("HW05Driver", "Driver")

                if not line in import_lines:

                    if line.startswith("import"):
                        import_lines.append(line);
                        outfile.write(line.encode())

                        continue
                    else:
                        code_lines.append(line.encode())
                
            code_lines.append("\n".encode())

    outfile.writelines(code_lines)
