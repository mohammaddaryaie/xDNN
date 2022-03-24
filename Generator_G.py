import numpy as np
import yelp.Functions_RNN as Functions_RNN

#Real Input + Shadow Input together
def Training_Generator_Main_MC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_main_cluster_inputs(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Test_Generator_Main_MC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_main_cluster_inputs(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Training_Generator_main_for_test_MC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_main_cluster_inputs_test(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels

#Shadow Inputs
def Training_Generator_Main_JC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_with_cluster(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Test_Generator_Main_JC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_with_cluster(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Training_Generator_main_for_test_JC(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func_with_cluster_test(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
#Real Inputs
def Training_Generator_Main(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Test_Generator_Main(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels
def Training_Generator_main_for_test(inputPath, bs: object, lb: object, mode: object = "train", aug: object = None) :
    # open the CSV file for reading
    f = open(inputPath, "r")
    while True:
        # initialize our batches of images and labels
        samples = []
        labels = []
        counter = 0
        #print('File Train: ' + inputPath)
        # keep looping until we reach our batch size
        while counter < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            #if counter==0:
             #   print(line)
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                line = f.readline()

                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                #if mode == "eval":
                 #   break

            # extract the label and construct the image
            line_error = line
            samples.append(Functions_RNN.main_func(line))
            line = line.strip().split(",")
            label = '1' if float(line[1]) ==5 else '0'
            labels.append(label)
            counter = counter + 1
        # one-hot encode the labels
        labels = lb.transform(np.array(labels))
        yield np.array(samples, dtype=np.float32), labels

