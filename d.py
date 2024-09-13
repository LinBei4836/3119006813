import sys
import hashlib

# 文件读写类
class Txt_IO:
    @staticmethod
    def readTxt(filePath):
        """读取文件内容并返回字符串"""
        with open(filePath, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def writeTxt(content, filePath):
        """将字符串写入文件"""
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(content)

# SimHash 生成类
class SimHash:
    @staticmethod
    def getSimHash(text):
        """根据输入的文本生成 SimHash 值"""
        words = text.split()
        hash_bits = [0] * 64  # SimHash 的长度一般是 64 位

        for word in words:
            # 对每个词求哈希
            word_hash = int(hashlib.md5(word.encode('utf-8')).hexdigest(), 16)
            for i in range(64):
                if word_hash & (1 << i):
                    hash_bits[i] += 1
                else:
                    hash_bits[i] -= 1

        # 将每一位结果转换为最终的 hash 值
        simhash = 0
        for i in range(64):
            if hash_bits[i] > 0:
                simhash |= (1 << i)

        return simhash

# 海明距离计算类
class Hamming:
    @staticmethod
    def getHammingDistance(hash1, hash2):
        """计算两个 SimHash 值之间的海明距离"""
        x = hash1 ^ hash2
        dist = 0
        while x:
            dist += 1
            x &= x - 1  # 清除最右边的1
        return dist

# 主程序类
class Main:
    @staticmethod
    def main(args):
        if len(args) != 4:
            print("Usage: python main.py <原文文件> <抄袭版文件> <答案文件>")
            return

        # 从命令行读取文件路径
        original_file = args[1]
        plagiarized_file = args[2]
        output_file = args[3]

        # 读取原文和抄袭版内容
        original_text = Txt_IO.readTxt(original_file)
        plagiarized_text = Txt_IO.readTxt(plagiarized_file)

        # 计算两个文本的 SimHash 值
        original_hash = SimHash.getSimHash(original_text)
        plagiarized_hash = SimHash.getSimHash(plagiarized_text)

        # 计算两个 SimHash 值的海明距离
        hamming_distance = Hamming.getHammingDistance(original_hash, plagiarized_hash)

        # 计算相似度，保留两位小数，SimHash 的长度是 64 位
        similarity = 1 - (hamming_distance / 64)
        similarity_percentage = round(similarity * 100, 2)

        # 将相似度结果写入输出文件
        Txt_IO.writeTxt(f"{similarity_percentage}\n", output_file)

        print(f"相似度: {similarity_percentage}%")

if __name__ == "__main__":
    Main.main(sys.argv)
import cProfile

def slow_function():
    total = 0
    for i in range(1, 100000):
        total += i
    return total

def fast_function():
    return sum([i for i in range(10000)])

def main():
    slow_function()
    fast_function()

if __name__ == "__main__":
    cProfile.run('main()')
if __name__ == "__main__":
    cProfile.run('main()', 'output.prof')
import pstats

p = pstats.Stats('output.prof')
p.sort_stats('tottime').print_stats(10)  # 按总时间排序，显示前10行
