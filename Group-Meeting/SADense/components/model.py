from keras import Model
from keras.backend import expand_dims
from keras.layers import *
import tensorflow.compat.v1 as tf
from components.layer import AngularConv, SpatialConv
from components.layer.backend import DenseCorrelation


def create_model(patch_sz, config):
    inp = Input(shape=[*config.a_in, *patch_sz])
    x = Lambda(lambda x_: expand_dims(x_, -1))(inp)
    activation = config.activation

    x = DenseCorrelation(
        dense_s=config.dense_s,
        dense_a=config.dense_a,
        dense_i=config.dense_i,
        corr_block_n=config.corr_block_n,
        corr_block_s=config.corr_block_s,
        corr_block_a=config.corr_block_a,
        corr_block_flt=config.corr_block_flt,
        activation=activation
    )(x)
    x = SpatialConv(64, (3, 3),
                        strides=(1, 1),
                        padding='same',
                        activation=activation,
                        name='reduce0'
                        )(x)
    x = SpatialConv(64, (3, 3),
                    strides=(1, 1),
                    padding='same',
                    activation=activation,
                    name='reduce1'
                    )(x)
    x = AngularConv(config.a_syn, (2, 2),
                    strides=(1, 1),
                    padding='valid',
                    activation=activation,
                    name='reduce2'
                    )(x)

    x = Reshape((patch_sz[0], patch_sz[1], config.a_syn))(x)
    out = Permute((3, 1, 2), name='out')(x)

    model = Model(inputs=inp, outputs=out)

    return model

def count_parameters():
    total_params = 0
    for variable in tf.trainable_variables():
        shape = variable.get_shape()
        variable_params = 1
        for dim in shape:
            variable_params *= dim.value
        total_params += variable_params
    return total_params

def count_flops():
    flops = tf.profiler.profile(tf.get_default_graph(),
                                options=tf.profiler.ProfileOptionBuilder.float_operation())
    return flops.total_float_ops

if __name__ == "__main__":
    # input_tensor = tf.random.normal((1, 4, 98, 98))
    from components.config import Config
    # 构建模型
    # input_tensor = tf.placeholder(tf.float32, shape=(1, 1, 128, 128))
    output_tensor, _ = create_model((96,96),Config)
    import time
    stat_time = time.time()
    # 计算参数数量和FLOPs
    num_params = count_parameters() / 1e6  # 转换为以百万（M）为单位
    flops = count_flops() / 1e9  # 转换为以十亿（G）为单位
    end_time = time.time()
    print("参数数量:", num_params, "M")
    print("FLOPs:", flops, "G")
    print(end_time - stat_time)