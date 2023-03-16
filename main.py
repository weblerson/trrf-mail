from driver import Driver, Elements, Using
from utils import Utils

if __name__ == '__main__':
    elements: Elements = Elements(
        name='//*[@id="wpcf7-f1181-p802-o1"]/form/p[1]/label[1]/span/input',
        email='//*[@id="wpcf7-f1181-p802-o1"]/form/p[1]/label[2]/span/input',
        subject='//*[@id="wpcf7-f1181-p802-o1"]/form/p[1]/label[3]/ \
                span/select',
        message='//*[@id="wpcf7-f1181-p802-o1"]/form/p[1]/label[4]/ \
                span/textarea'
    )

    driver: Driver = Driver(elements)

    for i in range(20):
        driver.enter_page(Utils.read_toml('env', 'url'))
        title = driver.get_title()

        driver.write_in_element(
            Using.XPATH,
            element='name',
            text='Lersinho'
        )

        name_input_text = driver.get_element_value(Using.XPATH, element='name')
        print(f'E-mail {i} enviado!\n')

    driver.exit()
