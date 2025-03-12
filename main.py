from tp1.root_finding import continu

if __name__ == "__main__":
    s1 = continu(1)
    s2 = continu(2)
    s3 = continu(1e-151)
    print(s1, s2, s3)
