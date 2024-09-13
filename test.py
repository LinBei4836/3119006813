class TestTxtIO(unittest.TestCase):
    def test_readTxt(self):
        # 创建临时文件，写入内容，然后读取
        test_file = 'test.txt'
        expected_content = 'This is a test.'
        Txt_IO.writeTxt(expected_content, test_file)
        content = Txt_IO.readTxt(test_file)
        self.assertEqual(content, expected_content)

    def test_writeTxt(self):
        # 测试文件写入功能
        test_file = 'write_test.txt'
        content = 'Writing test content.'
        Txt_IO.writeTxt(content, test_file)
        with open(test_file, 'r', encoding='utf-8') as file:
            read_content = file.read()
        self.assertEqual(read_content, content)

class TestSimHash(unittest.TestCase):
    def test_getSimHash(self):
        text1 = "This is a simple test."
        text2 = "This is a simple test!"
        hash1 = SimHash.getSimHash(text1)
        hash2 = SimHash.getSimHash(text2)
        self.assertIsInstance(hash1, int)
        self.assertIsInstance(hash2, int)

        # Hashes should be different for these two similar strings
        self.assertNotEqual(hash1, hash2)

class TestHamming(unittest.TestCase):
    def test_getHammingDistance(self):
        # 测试海明距离
        hash1 = int('101010', 2)
        hash2 = int('111010', 2)
        distance = Hamming.getHammingDistance(hash1, hash2)
        self.assertEqual(distance, 1)

    def test_zero_hamming_distance(self):
        # 如果两个哈希值相同，海明距离应为 0
        hash1 = int('101010', 2)
        hash2 = int('101010', 2)
        distance = Hamming.getHammingDistance(hash1, hash2)
        self.assertEqual(distance, 0)

class TestMainProgram(unittest.TestCase):
    def test_main_program(self):
        # 进行主程序的集成测试
        original_content = "This is the original text."
        plagiarized_content = "This is the plagiarized text."
        original_file = 'original.txt'
        plagiarized_file = 'plagiarized.txt'
        output_file = 'output.txt'

        # 写入测试文件
        Txt_IO.writeTxt(original_content, original_file)
        Txt_IO.writeTxt(plagiarized_content, plagiarized_file)

        # 模拟命令行参数
        sys.argv = ['main.py', original_file, plagiarized_file, output_file]

        # 运行主程序
        Main.main(sys.argv)

        # 验证输出结果
        with open(output_file, 'r', encoding='utf-8') as file:
            similarity = float(file.read().strip())
        self.assertTrue(0 <= similarity <= 100)

if __name__ == '__main__':
    unittest.main()
