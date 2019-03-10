### Description:
Tests written on pytests+request for this [api](https://qa-test-develop.marlin.onnisoft.com/swagger/index.html) 

### Run instruction:
```
git clone git@github.com:mpolynskyi/onnisoft-api-tests.git
cd onnisoft-api-tests
docker build -t onnisoft . && docker run -it onnisoft
```
### Notes:
Some tests are failing because there is bug,
some tests failing because not all endpoints are available,
some tests failing because of wrong/broken Bearer token.
I would like to explain every not clear place, please contact with me!