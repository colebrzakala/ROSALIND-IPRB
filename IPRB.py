def inheritance(fname):
    file = open(fname, 'r')
    s = file.read()
    file.close()
    nums = s.split(" ");
    k = float(nums[0]);
    m = float(nums[1]);
    n = float(nums[2]);
    t = k+m+n;
    p1 = (k/t)*((k-1)/(t-1));
    p2 = 2*(k/t)*((m)/(t-1));
    p3 = 2*(k/t)*((n)/(t-1));
    p4 = 0.75*(m/t)*((m-1)/(t-1));
    p5 = 0.5*(n/t)*(m/(t-1));
    p6 = 0.5*(m/t)*(n/(t-1));
    prob = p1+p2+p3+p4+p5+p6;
    return prob;
