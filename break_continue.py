def run():
    for i in range(1000):
        print(i)
        if i == 300:
            break
    print("Hemos terminado por el break")



if __name__ == '__main__':
    run()