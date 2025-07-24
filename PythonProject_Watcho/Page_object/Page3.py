from selenium.webdriver.common.by import By
import openpyxl


class Channel_Table:
    def __init__(self,driver):
        self.driver = driver
        self.table_locator = (By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div/div/section")
        self.cell_locator = (By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div/div/section/div/div[1]/div/div[2]")

    def channel_guide(self):

        Channel_cell = self.driver.find_elements(*self.cell_locator)
        Channel_cell_text = [row.text for row in Channel_cell]
        book = openpyxl.load_workbook("C:\\Users\\HP\\PycharmProjects\\PythonProject_Watcho\\test_cases\\Test_download.xlsx")
        sheet = book.active

        sheet.append(Channel_cell_text)

        try:
            sheet.append(Channel_cell_text)
            print("✅ Data appended.")
        except Exception as e:
            print("❌ Append failed:", e)

        book.save("C:\\Users\\HP\\PycharmProjects\\PythonProject_Watcho\\test_cases\\Test_download.xlsx")
        book.close()
