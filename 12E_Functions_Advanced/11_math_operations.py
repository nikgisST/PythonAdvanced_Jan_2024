def math_operations(*args, **kwargs):
    keys = list(kwargs.keys())  # [a, s, d, m]

    for i in range(len(args)):
        key = keys[i % 4]  # 0, 1, 2, 3
        key = keys[i % len(kwargs.keys())]

        if key == "a":
            kwargs[key] += args[i]
        elif key == "s":
            kwargs[key] -= args[i]
        elif key == "d":
            if args[i] != 0:
                kwargs[key] /= args[i]
        elif key == "m":
            kwargs[key] *= args[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)      # няма тук .items защото sorted връща tuple


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))