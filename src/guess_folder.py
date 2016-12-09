import tensorflow as tf
import sys
import os
import glob

def get_jpegs(path):
    for file in os.listdir(path):
        filepath = os.path.join(path,file)
        if os.path.splitext(filepath)[1] == '.jpg':
            yield filepath

images = list(get_jpegs('/mnt/test_images'))
if len(images) == 0:
    raise Exception('Cannot guess, no images found.')


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("/mnt/model/retrained_labels.txt")]
output_line = '{: <20}' + ''.join(['{: <15}' for x in label_lines])
print(output_line.format('image_name', *label_lines))

# Unpersists graph from file
with tf.gfile.FastGFile("/mnt/model/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    for image_path in images:
        print_list = [os.path.basename(image_path)[:-4]]

        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

        print_list += ['{:.2f}%'.format(p) for p in predictions[0]]
        print(output_line.format(*print_list))
