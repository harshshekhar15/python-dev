# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# print(f"fruit_list1: {fruit_list1}")
# print(f"fruit_list2: {fruit_list2}")
# print(f"fruit_list3: {fruit_list3}")
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# print(f"fruit_list1: {fruit_list1}")
# print(f"fruit_list2: {fruit_list2}")
# print(f"fruit_list3: {fruit_list3}")
 
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     print(f"ls: {ls}")
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
 
# print(sum)
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("python-dev")

def populate_list(num):
    try:
        result = []
        time.sleep(2)
        for i in range(10):
            result.append(num+i)
        return result
    except Exception as e:
        logger.error(f"Error populating list")

def process_file_for_pii():
    try:
        num = 10
        pii_data = []
        
        futures = []
        with ProcessPoolExecutor(max_workers=2) as executor:
            for _ in range(10):
                # text = str(chunks)
                futures.append(executor.submit(populate_list, num))
                if len(futures) >= 6:
                    logger.info(f"Waiting for batch of 6 chunks to complete.")
                    for future in as_completed(futures):
                        try:
                            result = future.result()
                            if result:
                                pii_data.extend(result)
                        except Exception as e:
                            logger.error(f"Error in future result: {e}")
                    futures = []
                # total_length += len(text)
                num += 10

            if futures:
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        if result:
                            pii_data.extend(result)
                    except Exception as e:
                        logger.error(f"Error in future result: {e}")
        return pii_data
    except Exception as e:
        logger.error(f"Error processing file for PII: {e}")
        
        
result = process_file_for_pii()
print(f"Result: {result}")