from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('samsung-internet-blog-posts.txt', num_epochs=20)

textgen.generate()
