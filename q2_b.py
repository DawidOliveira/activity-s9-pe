try:
    from scipy import stats
except ImportError:
    print('você não tem o scipy instalado, por favor execute o seguinte comando:\npip install scipy\n\nor\n\npip3 install scipy')
    exit()

def q2_b():
    size = [128, 256, 384, 512, 640, 768, 896, 1024]

    obs1 = [386, 850, 1544, 3035, 6650, 13887, 28059, 50916]
    obs2 = [375, 805, 1644, 3123, 6839, 14567, 27439, 52129]
    obs3 = [393, 824, 1553, 3235, 6768, 13456, 27659, 51360]

    meanObs = [384.66,826.33, 1580.33, 3131.33, 6722.33, 13970, 27719, 51468.33]

    m, b, r_value, p_value, std_err = stats.linregress(size, meanObs)

    print("m: {}, b: {}".format(m, b))

q2_b()