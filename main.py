def read_lines(file):
    with open(file, "r") as reader:
        return reader.readlines()


def write_lines(contents, file):
    with open(file, "w") as writer:
        writer.writelines(contents)


def transform_to_row(infile, outfile):
    with open(infile, "r") as reader:
        content = reader.read()
    write_lines([line + "\n" for line in content.rsplit(",")], outfile)


def add_greeting(infile, outfile):
    greeting = "Hello "
    write_lines([greeting + line for line in read_lines(infile)], outfile)


def strip_greeting(infile, outfile):
    greeting = "Hello "
    write_lines([line.removeprefix(greeting) for line in read_lines(infile)], outfile)


def combine_files(file1, file2, outfile):
    write_lines([line1.removesuffix("\n") + " " + line2 for (line1, line2) in
                 zip(read_lines(file1), read_lines(file2), strict=True)], outfile)
