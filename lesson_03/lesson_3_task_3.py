from address import Address
from mailing import Mailing


from_address = Address('614000', 'Perm', 'Lenina', '24', '185')
to_address = Address('101000', 'Москва',"Тверская", "54","21")
package = Mailing(to_address, from_address, 1099, "TR6541234")

print(f"Отправление {package.track} из {package.from_address} в {package.to_address}. Стоимость {package.cost} рублей.")
