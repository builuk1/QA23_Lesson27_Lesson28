# # Инкапсуляция
# # Инкапсулированный метод или поле, нельзя вызвать напрямую, только, через другие методы или поля
# # публичный — public        variable
# # защищенный — protected    _variable
# # приватный — private       __variable
# import datetime
#
#
# class Mobile:
#     color = 'red'  # поле класс,
#     ram = 4  # public публичное, можно обращаться без ограничений
#     _storage = 32  # protected
#     __model = 'Xiaomi'
#     imei = 123
#
#     def show_time(self):
#         return datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
#
#     def _change_ram(self, new_ram):
#         self.ram = new_ram
#
#     def __change_imei(self, new_imei):
#         self.imei = new_imei
#
#     def service_work(self, new_imei):
#         self.__change_imei(new_imei)
#
#
# mi8 = Mobile()
# # print(mi8.ram)
# # mi8.ram = 8
# # print(mi8.ram)
# # print(mi8._storage)
# # mi8._storage = 8
# # print(mi8._storage)
# #
# # print(mi8.show_time())
# # print(mi8.ram)
# # mi8._change_ram(12)
# # print(mi8.ram)
# # print(mi8.__model)
# mi8.__model = 'IPhone'  # Создаётся новое поле, не имеющее отношения к приватному
# print(mi8.imei)
# # mi8.__change_imei(456)#Это не будет работать
# mi8._Mobile__change_imei(456)  # Так можно обойти инкапсуляцию, но не нужно
# print(mi8.imei)
# mi8.service_work(789)
# print(mi8.imei)
#
#
# # Полиморфизм
#
# class Blender:
#     def cut(self, product):
#         if product == 'ice':
#             return 'icecream'
#         elif product == 'meat':
#             return 'mince'
#         else:
#             return 'cut ' + product
#
#
# slicer = Blender()
# print(slicer.cut('ice'))
# print(slicer.cut('meat'))
# print(slicer.cut('tree'))
#

class Storage:
    __money = 0

    def __change_money(self, count):
        if count > 0:
            self.__money = self.__money + count

    def deposite(self, secret_key, count):
        if secret_key == 'qwerty':
            self.__change_money(count)


FortNox = Storage()
FortNox.deposite('qwerty', 1000)
#'Hello World' > 40D1362A9442C634D6022B0050E0F0D0AA1E5666



