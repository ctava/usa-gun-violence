all: \
	us-albers.json

clean:
	rm -rf -- County_2010Census_DP1.*

County_2010Census_DP1.zip:
	curl -o $@ --raw 'http://www2.census.gov/geo/tiger/TIGER2010DP1/County_2010Census_DP1.zip'

County_2010Census_DP1.shp: County_2010Census_DP1.zip
	rm -rf $(basename $@)
	mkdir -p $(basename $@)
	unzip -d $(basename $@) $<
	for file in $(basename $@)/*; do chmod 644 $$file; mv $$file $(basename $@).$${file##*.}; done
	rmdir $(basename $@)
	touch $@

# projected (giving node extra memory since input shapefile is big)
us-albers.json: County_2010Census_DP1.shp
	node --max_old_space_size=8192 node_modules/.bin/topojson \
		-q 1e5 \
		-s 1 \
		--projection 'd3.geo.albersUsa()' \
		--id-property=GEOID10 \
		-p name=NAMELSAD10,pop=+DP0010001 \
		-o $@ \
		-- counties=County_2010Census_DP1.shp

# non-projected (not used by this example, but included for reference)
us.json: County_2010Census_DP1.shp
	node_modules/.bin/topojson \
		-q 1e5 \
		-s 7e-7 \
		--id-property=GEOID10 \
		-p name=NAMELSAD10,pop=+DP0010001 \
		-o $@ \
		-- counties=County_2010Census_DP1.shp