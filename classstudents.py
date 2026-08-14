class student:
    count=1
    def increment(self):
        self.count=self.count+1
        print(self.count)
    def __init__(self):
        self.count=self.count()+1
        print(self.count)
s1=student();
s2=student();
s3=student();
s1.increment()