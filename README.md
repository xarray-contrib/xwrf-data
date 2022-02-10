[![CI](https://github.com/ncar-xdev/xwrf-data/actions/workflows/ci.yaml/badge.svg)](https://github.com/ncar-xdev/xwrf-data/actions/workflows/ci.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ncar-xdev/xwrf-data/main.svg)](https://results.pre-commit.ci/latest/github/ncar-xdev/xwrf-data/main)

# xwrf-data

Data repository for xwrf documentation, tutorials, testing

## Sample data sets

These files are used as sample data in xwrf testing suites, tutorials, and documentation. These data sets can be downloaded via the [`xwrf`](https://github.com/ncar-xdev/xwrf) tutorial module. See the documentation for more information.

- [`dummy.nc`](./data/dummy.nc): A dummy file for testing purposes
- [`dummy_attrs_only.nc`](./data/dummy_attrs_only.nc): A dummy file with only attributes for testing purposes
- [`geo_em_d01_polarstereo.nc`](./data/geo_em_d01_polarstereo.nc): polar stereographic sample from [Salem](https://github.com/fmaussion/salem-sample-data/blob/master/salem-test/grid/geo_em_d01_polarstereo.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`geo_em_d02_polarstereo.nc`](./data/geo_em_d02_polarstereo.nc): polar stereographic with inner nest sample from [Salem](https://github.com/fmaussion/salem-sample-data/blob/master/salem-test/grid/geo_em_d02_polarstereo.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`lambert_conformal_sample.nc`](./data/lambert_conformal_sample.nc): Retrieved from <https://api.blika.is/static/wrfout_example.nc>
- [`mercator_sample.nc`](./data/mercator_sample.nc): Retrieved from [NCAR/wrf-pyton](https://github.com/NCAR/wrf-python/blob/develop/test/ci_tests/ci_test_file.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`tiny.nc`](./data/tiny.nc): A tiny file for testing purposes
