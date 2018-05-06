package main

import (
	"bufio"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"strings"

	"github.com/kniren/gota/dataframe"
	"github.com/kniren/gota/series"
)

var (
	//hostname = "https://usa-gun-violence.appspot.com"
	hostname = "http://localhost:8080"
	//endpoint = "/data"
	endpoint = "/yearsummary"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func callService(hostname, endpoint, year, month, n_injured, n_killed string) error {

	data := url.Values{}
	data.Set("year", year)
	data.Set("month", month)
	data.Set("n_injured", n_injured)
	data.Set("n_killed", n_killed)

	client := &http.Client{}
	u, _ := url.ParseRequestURI(hostname + endpoint + "?year=" + year + "&month=" + month + "&n_injured=" + n_injured + "&n_killed=" + n_killed)
	urlStr := fmt.Sprintf("%v", u)
	method := "PUT"
	req, err := http.NewRequest(method, urlStr, nil)
	//req, err := http.NewRequest(method, urlStr, bytes.NewBufferString(data.Encode()))
	req.Header.Add("Content-Type", "application/json")
	//req.Header.Add("Content-Length", strconv.Itoa(len(data.Encode())))
	fmt.Println(req)
	resp, err := client.Do(req)
	fmt.Println(resp)
	if err != nil {
		fmt.Println(err)
		return err
	}

	return nil
}

func putYearSummaryByMonth(hostname, endpoint, year string) {

	for i := 1; i < 13; i++ {
		month := fmt.Sprintf("%02d", i)
		fileName := fmt.Sprintf("%s-%s.csv", year, month)
		f, err := os.Open(fileName)
		check(err)
		r := bufio.NewReader(f)
		df := dataframe.ReadCSV(r)
		sum := func(s series.Series) series.Series {
			floats := s.Float()
			sum := 0.0
			for _, f := range floats {
				sum += f
			}
			return series.Floats(sum)
		}
		n_injured := df.Select([]string{"n_injured"}).Capply(sum).Records()
		n_killed := df.Select([]string{"n_killed"}).Capply(sum).Records()
		err = callService(hostname, endpoint, year, month, fmt.Sprintf("%s", strings.TrimRight(n_injured[1][0], ".000000")), fmt.Sprintf("%s", strings.TrimRight(n_killed[1][0], ".000000")))
		check(err)
	}

}

func main() {

	year := "2013"
	putYearSummaryByMonth(hostname, endpoint, year)
	year = "2014"
	putYearSummaryByMonth(hostname, endpoint, year)
	year = "2015"
	putYearSummaryByMonth(hostname, endpoint, year)
	year = "2016"
	putYearSummaryByMonth(hostname, endpoint, year)
	year = "2017"
	putYearSummaryByMonth(hostname, endpoint, year)
	year = "2018"
	putYearSummaryByMonth(hostname, endpoint, year)
}
