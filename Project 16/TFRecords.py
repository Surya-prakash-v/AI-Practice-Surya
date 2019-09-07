from random import shuffle
import glob
shuffle_data = True  # shuffle the addresses before saving
cifar_10_data_path = 'Cat vs Dog/train/*.jpg'
# read addresses and labels from the 'train' folder
addrs = glob.glob(cifar_10_data_path)
labels = [0 if 'cat' in addr else 1 for addr in addrs]  # 0 = Cat, 1 = Dog
# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)
  
def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

# Divide the data into 60% train, 20% validation, and 20% test
createTFRecordFile('train_file',0,int(0.6*len(addrs)))

createTFRecordFile('val_file',int(0.6*len(addrs)),int(0.8*len(addrs)))

createTFRecordFile('test_file',int(0.8*len(addrs)),len(addrs))

def createTFRecordFile(filename,addrs,labels):
  # open the TFRecords file
  writer = tf.python_io.TFRecordWriter(filename)
  for i in range(len(addrs)):
    # print how many images are saved every 1000 images
    if not i % 1000:
        print str(name) + ' data: {}/{}'.format(i, len(addrs))
        sys.stdout.flush()
    # Load the image
    img = cv2.imread(addrs[i])
    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32)
    
    label = labels[i]
    # Create a feature
    feature = {'filename/label': _int64_feature(label),
               'filename/image': _bytes_feature(tf.compat.as_bytes(img.tostring()))}
    # Create an example protocol buffer
    example = tf.train.Example(features=tf.train.Features(feature=feature))
    
    # Serialize to string and write on the file
    writer.write(example.SerializeToString())
    
  writer.close()
  sys.stdout.flush()


