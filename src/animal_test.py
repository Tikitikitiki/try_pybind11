import animal


def main():
    simba = animal.Animal("Simba")
    simba.set_hobby("volleyball")
    print(f'python: name: {simba.get_name()}\t hobby: {simba.get_hobby()}')
    simba.print_animal()


if __name__ == "__main__":
    main()
