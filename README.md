[![CI](https://github.com/ncar-xdev/xwrf-data/actions/workflows/ci.yaml/badge.svg)](https://github.com/ncar-xdev/xwrf-data/actions/workflows/ci.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ncar-xdev/xwrf-data/main.svg)](https://results.pre-commit.ci/latest/github/ncar-xdev/xwrf-data/main)

# xwrf-data

Data repository for xwrf documentation, tutorials, testing

## Sample data sets

These files are used as sample data in xwrf testing suites, tutorials, and documentation. These data sets can be downloaded via the [`xwrf`](https://github.com/ncar-xdev/xwrf) tutorial module. See the documentation for more information.

- [`dummy.nc`](./data/dummy.nc): A dummy file for testing purposes
- [`dummy_attrs_only.nc`](./data/dummy_attrs_only.nc): A dummy file with only attributes for testing purposes
- [`dummy_salem_parsed.nc`](./data/dummy_salem_parsed.nc): `dummy.nc` as parsed by [Salem](https://github.com/fmaussion/salem) for testing purposes
- [`geo_em_d01_polarstereo.nc`](./data/geo_em_d01_polarstereo.nc): Polar stereographic sample from [Salem](https://github.com/fmaussion/salem-sample-data/blob/master/salem-test/grid/geo_em_d01_polarstereo.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`geo_em_d02_polarstereo.nc`](./data/geo_em_d02_polarstereo.nc): Polar stereographic with inner nest sample from [Salem](https://github.com/fmaussion/salem-sample-data/blob/master/salem-test/grid/geo_em_d02_polarstereo.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`lambert_conformal_sample.nc`](./data/lambert_conformal_sample.nc): Retrieved from <https://api.blika.is/static/wrfout_example.nc>
- [`mercator_sample.nc`](./data/mercator_sample.nc): Retrieved from [NCAR/wrf-pyton](https://github.com/NCAR/wrf-python/blob/develop/test/ci_tests/ci_test_file.nc?rgh-link-date=2022-02-07T21%3A50%3A37Z)
- [`ideal.nc`](./data/ideal.nc): Idealised (cartesian) sample
- [`tiny.nc`](./data/tiny.nc): A tiny file for testing purposes
- [`met_em.d01.2005-08-28_12:00:00.nc`](./data/met_em.d01.2005-08-28_12:00:00.nc): Metgrid ouput from [openwfm](https://wiki.openwfm.org/wiki/How_to_run_WRF-Fire_with_real_data)
- [`wrfout_d01_2099-10-01_00:00:00.nc`](./data/wrfout_d01_2099-10-01_00:00:00.nc): CMIP6 GCMs downscaled using WRF, accessed on 2022-09-16 from https://registry.opendata.aws/wrf-cmip6.

## Sample Intake Catalog

We also include an [intake](https://github.com/intake/intake) catalog, which makes use of [intake-xarray](https://github.com/intake/intake-xarray).

You can access this data catalog using the following syntax:

```python
import intake

# Read in the data catalog from github
cat = intake.open_catalog('https://raw.githubusercontent.com/xarray-contrib/xwrf-data/main/catalogs/catalog.yml')

# Read one of the sample datasets
ds = cat["xwrf-sample-ssp245"].to_dask()

ds
```

```
<xarray.Dataset>
Dimensions:                (Time: 124, south_north: 340, west_east: 270,
                            bottom_top_stag: 40, bottom_top: 39,
                            soil_levels_or_lake_levels_stag: 10,
                            snow_and_soil_levels_stag: 15, soil_layers_stag: 4,
                            seed_dim_stag: 2, west_east_stag: 271,
                            south_north_stag: 341, snow_layers_stag: 3,
                            interface_levels_stag: 16, snso_layers_stag: 7)
Coordinates:
  * Time                   (Time) float64 nan 1.0 2.0 3.0 ... 121.0 122.0 123.0
    XLAT                   (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    XLAT_U                 (Time, south_north, west_east_stag) float32 dask.array<chunksize=(1, 340, 271), meta=np.ndarray>
    XLAT_V                 (Time, south_north_stag, west_east) float32 dask.array<chunksize=(1, 341, 270), meta=np.ndarray>
    XLONG                  (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    XLONG_U                (Time, south_north, west_east_stag) float32 dask.array<chunksize=(1, 340, 271), meta=np.ndarray>
    XLONG_V                (Time, south_north_stag, west_east) float32 dask.array<chunksize=(1, 341, 270), meta=np.ndarray>
    XTIME                  (Time) float32 dask.array<chunksize=(1,), meta=np.ndarray>
Dimensions without coordinates: south_north, west_east, bottom_top_stag,
                                bottom_top, soil_levels_or_lake_levels_stag,
                                snow_and_soil_levels_stag, soil_layers_stag,
                                seed_dim_stag, west_east_stag,
                                south_north_stag, snow_layers_stag,
                                interface_levels_stag, snso_layers_stag
Data variables: (12/283)
    ACGRDFLX               (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ACHFX                  (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ACLHF                  (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ACLWDNB                (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ACLWDNBC               (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ACLWDNT                (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    ...                     ...
    ZNU                    (Time, bottom_top) float32 dask.array<chunksize=(1, 39), meta=np.ndarray>
    ZNW                    (Time, bottom_top_stag) float32 dask.array<chunksize=(1, 40), meta=np.ndarray>
    ZS                     (Time, soil_layers_stag) float32 dask.array<chunksize=(1, 4), meta=np.ndarray>
    ZSNSO                  (Time, snso_layers_stag, south_north, west_east) float32 dask.array<chunksize=(1, 7, 340, 270), meta=np.ndarray>
    ZWT                    (Time, south_north, west_east) float32 dask.array<chunksize=(1, 340, 270), meta=np.ndarray>
    Z_LAKE3D               (Time, soil_levels_or_lake_levels_stag, south_north, west_east) float32 dask.array<chunksize=(1, 10, 340, 270), meta=np.ndarray>
Attributes: (12/149)
    ADAPT_DT_MAX:                    72.0
    ADAPT_DT_MIN:                    36.0
    ADAPT_DT_START:                  54.0
    AERCU_FCT:                       1.0
    AERCU_OPT:                       0
    AER_ANGEXP_OPT:                  1
    ...                              ...
    WEST-EAST_PATCH_END_STAG:        271
    WEST-EAST_PATCH_END_UNSTAG:      270
    WEST-EAST_PATCH_START_STAG:      1
    WEST-EAST_PATCH_START_UNSTAG:    1
    W_DAMPING:                       0
    YSU_TOPDOWN_PBLMIX:              0
```

This catalog includes the following virtual datasets created using [kerchunk](https://fsspec.github.io/kerchunk/):

- [`xwrf-sample-ssp245`](./catalogs/ssp245_gcm_wrfout_combined.json): WRF Downscaled CMIP6; SSP245; Combined virtual dataset (2099-10, d01)
- [`xwrf-sample-ssp585`](./catalogs/ssp585_gcm_wrfout_combined.json): WRF Downscaled CMIP6; SSP585; Combined virtual dataset (2099-10, d01)
- [`single-output-sample`](./catalogs/gcm_wrfout_d01_2099-10-01_00_00_00.json): Virtual WRF output dataset for testing purposes, consisting of a single time from xwrf-sample-ssp585 (2099-10-01T00:00)
