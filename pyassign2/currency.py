
from urllib.request import urlopen
def exchange(currency_from, currency_to, amount_from):
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    url+='from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstrs=jstr.replace('true','True')
    jstr=eval(jstrs)
    print(jstr['to'])
def test_exchange():
    assert('2.1589225Euros'==exchange('USD','EUR',2.5))
    assert('28.77882 Chinese Yuan'==exchange('USD','CNY',4.2))
    assert('0.52932528713825 Euros'==exchange('CNY','EUR',4.2))
def main():
    currency_from=input()
    currency_to=input()
    amount_from=input()
    test_exchange()
    exchange(currency_from,currency_to,amount_from)
if __name__=='__main__':
    main()
