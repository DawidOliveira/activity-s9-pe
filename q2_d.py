try:
    from scipy import stats
except ImportError:
    print('você não tem o scipy instalado, por favor execute o seguinte comando:\npip install scipy\n\nor\n\npip3 install scipy')
    exit()

def q2_d():
    size = [128, 256, 384, 512, 640, 768, 896, 1024]

    obs1 = [386, 850, 1544, 3035, 6650, 13887, 28059, 50916]
    obs2 = [375, 805, 1644, 3123, 6839, 14567, 27439, 52129]
    obs3 = [393, 824, 1553, 3235, 6768, 13456, 27659, 51360]

    meanObs = [384.66,826.33, 1580.33, 3131.33, 6722.33, 13970, 27719, 51468.33]

    m, b, r_value, p_value, std_err = stats.linregress(size, meanObs)

    b1 = m
    b0 = b
    print(f"b0: {b0:.4f}, b1: {b1:.4f}")
    print('------------------------')
    confidence_interval(size,meanObs)


def confidence_interval(x, y, p=0.90):
    tinv = lambda p, df: abs(stats.t.ppf(p/2, df))

    res = stats.linregress(x, y)
    ts = tinv((1-p), len(x)-2)
    print(f"{ts} * {res.intercept_stderr:.3f}")
    print(f"b0 ({p*100}%): {res.intercept:.4f}"
        f" +/- {ts*res.intercept_stderr:.4f}")
    print(f"b1 ({p*100}%): {res.slope:.4f} +/- {ts*res.stderr:.4f}")
    print('------------------------')
    print(f"b0 ({p*100}%): ({(res.intercept - ts*res.intercept_stderr):.4f}, {(res.intercept + ts*res.intercept_stderr):.4f})")
    print(f"b1 ({p*100}%): ({(res.slope - ts*res.stderr):.4f}, {(res.slope + ts*res.stderr):.4f})")
        

q2_d()
