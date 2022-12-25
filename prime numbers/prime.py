class Prime(object):
    def __init__(self):
        file = open('prime numbers.txt', 'r')
        self.primelist = file.read().split(',')
        file.close()

        file = open('binary primes.txt', 'r')
        self.searchlist = list(file.read())
        file.close()

        file = open('misc data.txt', 'r')
        self.max, self.len = map(int, file.read().split(','))
        file.close()

    def get_largest_prime(self):
        return self.primelist[-1]
    def get_nth_prime(self, n):
        if self.len < n:   #not enough primes in list
            self.generate_n_primes(n)
        return self.primelist[n - 1]

    def is_prime(self, num):
        #add more prime numbers if num is bigger
        if self.max < num:
            self.generate_prime(num)

        return self.searchlist[num] == '1'
    def is_prime_slow(self, num):  #for checking new prime numbers
        for n in self.primelist:
            n = int(n)
            if n ** 2 > num:  #only loop up to sqrt of num
                break

            if num % n == 0:  #divisible
                return False

        return True #is prime

    def generate_prime(self, end):  #add primes up to end
        while self.max < end:
            self.max += 1
            if self.is_prime_slow(self.max): #add to file and list
                self.add_prime(self.max)
                self.extend_search(1)
                self.len += 1

            else:                       #add 0 to binary list
                self.extend_search(0)
        
        file = open('misc data.txt', 'w')
        file.write(str(self.max) + ',' + str(self.len))
        file.close()
    def generate_n_primes(self, n):  #add number of primes up to n
        while self.len < n:
            self.generate_prime(self.max + 1)


    def add_prime(self, num):
        file = open('prime numbers.txt', 'a')
        file.write(',' + str(num))
        file.close()

        self.primelist.append(num)
    def extend_search(self, n):
        file = open('binary primes.txt', 'a')
        file.write(str(n))
        file.close()
        
        self.searchlist.append(n)

    def display_n_primes(self, n): #display first n prime numbers
        if self.len < n:   #not enough primes in list
            self.generate_n_primes(n)
            
        for i in range(n):
            print(self.primelist[i])
    def display_largest_prime(self):
        print(self.get_largest_prime())
    def display_nth_prime(self, n):
        print(self.get_nth_prime(n))


