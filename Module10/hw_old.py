from datetime import datetime
import multiprocessing


class WarehouseManager:
    data = {}

    def process_request(self, request):
        name, action, count = request
        if action == 'receipt':
            if name not in self.data:
                self.data[name] = count
            else:
                self.data[name] += count
        elif action == 'shipment':
            if name in self.data and self.data[name] > 0:
                self.data[name] -= count
            else:
                print('Такого товара не существует, либо нет в наличии!')
        else:
            print('Неверно указано действие!')

    def run(self, requests):
        


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(manager.data)
