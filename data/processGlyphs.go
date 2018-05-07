package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/kniren/gota/dataframe"
	"github.com/kniren/gota/series"
	"github.com/pkg/errors"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
	"gonum.org/v1/plot/vg"
)

type mnth struct {
	month     string
	n_injured string
	n_killed  string
}

var months []mnth

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	year := "2013"
	createGlyphSummaryByYear(year)
	year = "2014"
	createGlyphSummaryByYear(year)
	year = "2015"
	createGlyphSummaryByYear(year)
	year = "2016"
	createGlyphSummaryByYear(year)
	year = "2017"
	createGlyphSummaryByYear(year)
	year = "2018"
	createGlyphSummaryByYear(year)
}

func createGlyphSummaryByYear(year string) {
	months = nil
	for i := 1; i < 13; i++ {
		y, err := strconv.Atoi(year)
		check(err)
		if y == 2018 && i > 3 {
			break
		}
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
		addToGraphData(month, strings.TrimRight(n_injured[1][0], ".000000"), strings.TrimRight(n_killed[1][0], ".000000"))
	}
	makeGraph(year)
}

func addToGraphData(month, n_injured, n_killed string) {

	months = append(months, mnth{month, n_injured, n_killed})

}

func makeGraph(year string) {

	// Prepare the data for plotting
	xys1 := preparePlotData1()
	xys2 := preparePlotData2()

	// Create and save the plot.
	if err := makePlot(year, xys1, xys2); err != nil {
		log.Fatal(err)
	}
}

// preparePlotData prepares the raw input data for plotting.
func preparePlotData2() plotter.XYs {
	pts := make(plotter.XYs, len(months))
	var i int

	for _, month := range months {
		n_injured, err := strconv.ParseFloat(month.n_injured, 64)
		check(err)
		pts[i].Y = float64(n_injured)
		month, err := strconv.ParseFloat(month.month, 64)
		check(err)
		pts[i].X = float64(month)
		i++
	}

	return pts
}

// preparePlotData prepares the raw input data for plotting.
func preparePlotData1() plotter.XYs {
	pts := make(plotter.XYs, len(months))
	var i int

	for _, month := range months {
		n_killed, err := strconv.ParseFloat(month.n_killed, 64)
		check(err)
		pts[i].Y = float64(n_killed)
		month, err := strconv.ParseFloat(month.month, 64)
		check(err)
		pts[i].X = float64(month)
		i++
	}

	return pts
}

// makePlots makes the plots for the year-month.
func makePlot(year string, xys1, xys2 plotter.XYs) error {

	// Create a plot value.
	p, err := plot.New()
	if err != nil {
		return errors.Wrap(err, "Could not create plot object")
	}

	// Label the plot.
	p.Y.Label.Text = "People Affected"
	p.X.Label.Text = "Months"

	// Add both sets of points: n_injured, n_killed by month
	if err := plotutil.AddLinePoints(p, "", xys1, "", xys2); err != nil {
		return errors.Wrap(err, "Could not add lines to plot")
	}

	// Save the plot.
	if err := p.Save(2*vg.Inch, 2*vg.Inch, year+".png"); err != nil {
		return errors.Wrap(err, "Could not output plot")
	}

	return nil
}
