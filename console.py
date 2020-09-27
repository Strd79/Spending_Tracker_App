import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.user import User
import repositories.user_repository as user_repository

# user_1 = User("Billy", "Smith", "bsmith@yahoo.com", "BSaBc123")
# user_2 = User("David", "Strain", "strd79@hotmail.co.uk", "DSpw789")
# user_repository.save(user_1)
# user_repository.save(user_2)

# merchant_1 = Merchant("Tesco Express", "Frederick Street", "Birmingham", user_1)
# merchant_2 = Merchant("BP", "Birmingham Road", "West Bromwich", user_1)
# merchant_3 = Merchant("Morrisons", "Merkland Court", "Partick", user_2)
# merchant_4 = Merchant("Jack Wills", "Buchanan Street", "Glasgow", user_2)
# merchant_repository.save(merchant_1)
# merchant_repository.save(merchant_2)
# merchant_repository.save(merchant_3)
# merchant_repository.save(merchant_4)

# tag_1 = Tag("Food shopping", "This includes Food & drink shopping for eating at home.", user_1)
# tag_2 = Tag("Petrol - Private", "This includes cost of petrol for personal use.", user_1)
# tag_3 = Tag("Food & Drink", "This is for Food & drink shopping for eating at home.", user_2)
# tag_4 = Tag("Clothes", "This is for any clothes shopping I do.", user_2)
# tag_repository.save(tag_1)
# tag_repository.save(tag_2)
# tag_repository.save(tag_3)
# tag_repository.save(tag_4)

# transaction_1 = Transaction(merchant_1, "25 Sep 2020", 78.43, tag_1, user_1)
# transaction_2 = Transaction(merchant_2, "05 Aug 2020", 44.90, tag_2, user_1)
# transaction_3 = Transaction(merchant_3, "20 Sep 2020", 65.05, tag_3, user_2)
# transaction_4 = Transaction(merchant_4, "14 Jul 2020", 49.99, tag_4, user_2)
# transaction_repository.save(transaction_1)
# transaction_repository.save(transaction_2)
# transaction_repository.save(transaction_3)
# transaction_repository.save(transaction_4)

# print(merchant_repository.select_all())
# print(merchant_repository.select(4))
# merchant_repository.update(Merchant("Tesco", "Frederick Road", "Birmingham", user_1, 1))
# merchant_5 = Merchant("ASDA", "Frederick Street", "Birmingham", user_2)
# merchant_repository.save(merchant_5)
# merchant_repository.delete(5)
# transaction_repository.delete_all()
# merchant_repository.delete_all()
# tag_repository.delete_all()
# user_repository.delete_all()

# print(user_repository.select_all())
# print(user_repository.select(2))
# user_repository.update(User("Kyle", "Law", "abc@abcd.com", "password", 2))
# user_repository.delete(2)
# user_repository.delete_all()

# print(tag_repository.select_all())
# print(tag_repository.select(5))
# tag_repository.update(Tag("Test", "testing description", user_1, 8))
# tag_repository.delete(8)

# print(transaction_repository.select_all())
# print(transaction_repository.select(3))
# transaction_repository.update(Transaction(merchant_1, "08 Jan 2000", 123.45, tag_2, user_1, 1))
# transaction_repository.delete(4)

pdb.set_trace()