from score import Score
def key_rank(item):
    return item[1].sum
class ScoreManagementSystem:
    def __init__(self):
        self._score={}
    def read(self, score_data_file):
        if self._score != None :
            self._score={}
        
        with open(score_data_file, 'rt', encoding='utf-8') as fo:
            data =fo.read()
            lines = data.strip().split('\n')
        num = 0
        for line in lines:
            num += 1
            self._score[num] = Score(line.strip())
        return len(self._score)
 def _make_cars_string(self, score,order_key,order_way):
        result = ""
        temp_sum=0
        if order_way== 'asc':
            num =1
        elif order_way=='des':
            num = len(score)

        for key, item in score:
            result = result + str(item.no) +','
            result = result + item.name +','
@@ -38,15 +40,21 @@ def _make_cars_string(self, score,order_key,order_way):
            elif item.avg % 1 ==0:
                result = result + str(int(item.avg)) + ','

            if item.sum!=temp_sum:
                same_num = num

            if order_key =='register':
                result = result + str(key) + '\n'
            elif order_way== 'asc':
                result = result + str(num) + '\n'
                result = result + str(same_num) + '\n'
                num +=1
            elif order_way== 'des':
                result = result + str(num) + '\n'
                result = result + str(same_num) + '\n'
                num -=1

            temp_sum = item.sum
            temp_num = num

        return result.strip()