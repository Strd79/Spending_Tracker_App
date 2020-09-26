import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.user import User
import repositories.user_repository as user_repository

merchant_1 = Merchant("Tesco Express", "Frederick Street", "Birmingham")
merchant_2 = Merchant("BP", "Birmingham Road", "West Bromwich")
merchant_3 = Merchant("Morrisons", "Merkland Court", "Partick")
merchant_4 = Merchant("Jack Wills", "Buchanan Street", "Glasgow")
merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
merchant_repository.save(merchant_4)

tag_1 = Tag("Food shopping", "This includes Food & drink shopping for eating at home.")
tag_2 = Tag("Petrol - Private", "This includes cost of petrol for personal use.")
tag_3 = Tag("Clothes", "This is for any clothes shopping I do.")
tag_repository.save(tag_1)
tag_repository.save(tag_2)
tag_repository.save(tag_3)

transaction_1 = Transaction(merchant_1, "25 Sep 2020", 78.43, tag_1)
transaction_2 = Transaction(merchant_2, "05 Aug 2020", 44.90, tag_2)
transaction_3 = Transaction(merchant_3, "20 Sep 2020", 65.05, tag_1)
transaction_4 = Transaction(merchant_4, "14 Jul 2020", 49.99, tag_3)
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
transaction_repository.save(transaction_4)

user_1 = User("Billy", "Smith", "bsmith@yahoo.com", "BSaBc123")
user_2 = User("David", "Strain", "strd79@hotmail.co.uk", "DSpw789")
user_repository.save(user_1)
user_repository.save(user_2)

pdb.set_trace()