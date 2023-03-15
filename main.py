from driver import Driver
from utils import Utils

if __name__ == '__main__':
    driver: Driver = Driver()
    driver.enter_page(Utils.read_toml('env', 'url'))
    title = driver.get_title()

    print(title)

    driver.exit()