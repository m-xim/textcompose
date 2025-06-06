# CHANGELOG

<!-- version list -->

## v1.1.0 (2025-06-06)

### Bug Fixes

- Improve handling of string conditions in component logic (`when`)
  ([`b3cb4fc`](https://github.com/m-xim/textcompose/commit/b3cb4fc4b94dbd203c57233b2658955752798b7a))

### Features

- Add ProgressBar component with customizable styles
  ([`6d64998`](https://github.com/m-xim/textcompose/commit/6d64998173fb26c6e588fdfee2a43ecd5df8497c))

### Refactoring

- Rename container, logic, custom_component folders to plural form
  ([`b68bcc5`](https://github.com/m-xim/textcompose/commit/b68bcc56c11d5fab3dc97f4ef5f38ecde1fd5210))


## v1.0.0 (2025-06-01)

### Bug Fixes

- **tests**: Rename `then` to `then_`
  ([`27e3831`](https://github.com/m-xim/textcompose/commit/27e38314ad499fde1f7b5f790fe06a41d924f255))

- **tests**: Test_if.py
  ([`e9427a1`](https://github.com/m-xim/textcompose/commit/e9427a1b7ff500a51ac6f9a195435d8d9d246f56))

### Chores

- Add base example and update README
  ([`9d8f121`](https://github.com/m-xim/textcompose/commit/9d8f121723c96c2c3120022fa9618e701c852e53))

- Update README.md
  ([`d4854a4`](https://github.com/m-xim/textcompose/commit/d4854a4ee14e526ffb20b6b0e153b020b67f1152))

- **i18n**: Add example custom_component
  ([`9d0c517`](https://github.com/m-xim/textcompose/commit/9d0c51796954fe05c7d65945860284bd18344bac))

### Features

- Release version 1.0.0
  ([`5158350`](https://github.com/m-xim/textcompose/commit/5158350af25b9a89dcceee9acfb12bbdc65509f6))

- **container**: Add List to module exports and rename 'then' parameter in `If` class
  ([`1183c29`](https://github.com/m-xim/textcompose/commit/1183c29a2e80de7995f2f39725fc8fe4dca14304))

- **i18n**: Enhance I18nTC class with locale support and improved mapping resolution
  ([`94c2fbc`](https://github.com/m-xim/textcompose/commit/94c2fbc33f72ef1c83d76e893a59dfb3ddf1c0c2))

- **jinja**: Add Jinja rendering support
  ([`49601d0`](https://github.com/m-xim/textcompose/commit/49601d03ae1cedbd6b9f5aa92601d0b91255f144))

- **list**: Add List class for rendering items
  ([`06e7357`](https://github.com/m-xim/textcompose/commit/06e7357b93132d581dac13f77dda02bc91101423))

- **project**: Update project metadata and enhance README with features and usage examples
  ([`7f4fc4a`](https://github.com/m-xim/textcompose/commit/7f4fc4aa8902870edc6ec3190005d4c856a4bf22))

### Breaking Changes

- Introduced changes that break backward compatibility.


## v0.6.1 (2025-05-08)

### Bug Fixes

- **content**: Remove debug print statement and ensure proper handling of empty parts in rendering
  ([`0393f2a`](https://github.com/m-xim/textcompose/commit/0393f2aa19342f82ce7c88e465dbde3272c5a175))


## v0.6.0 (2025-05-08)

### Features

- **template**: Add separator option to Template for customizable rendering
  ([`a25b9b5`](https://github.com/m-xim/textcompose/commit/a25b9b55d22e9bdcc8ae5a2b2bebd950734baa0d))


## v0.5.0 (2025-05-08)

### Features

- **logical**: Add If class for conditional rendering logic
  ([`459e0e1`](https://github.com/m-xim/textcompose/commit/459e0e104cc2a3cb7436765d6b3f70795584d931))


## v0.4.0 (2025-05-04)

### Documentation

- Update README to enhance section headings with emojis
  ([`2b48887`](https://github.com/m-xim/textcompose/commit/2b48887aa1bb59cc5969cc53ba6ccdedf3bc693e))

### Features

- **content**: Update Value type to support callable for dynamic value resolution
  ([`2c90531`](https://github.com/m-xim/textcompose/commit/2c9053145eaa2b53ca044406bdae998a909e582d))


## v0.3.0 (2025-05-03)

### Bug Fixes

- **content**: Resolve circular import by moving resolve_value to BaseContent
  ([`a320b19`](https://github.com/m-xim/textcompose/commit/a320b19cc4115cce406e900bee67f7e0e87147ce))

### Features

- Add resolve_value and extend support for dynamic types in group, and template
  ([`e5bfaeb`](https://github.com/m-xim/textcompose/commit/e5bfaeb7ebb470483719eaef9354c8b08a7eac6a))


## v0.2.0 (2025-05-02)

### Chores

- **release**: Fix
  ([`365ad02`](https://github.com/m-xim/textcompose/commit/365ad025db2b580e16941d207491a18560034573))

- **release**: Migrate to single-branch workflow and manual release process
  ([`add9991`](https://github.com/m-xim/textcompose/commit/add9991277ceaa84afc324cace9d894b50a308c2))

### Features

- Custom arg in render
  ([`94fc405`](https://github.com/m-xim/textcompose/commit/94fc405c44f3aafa34a55dabf7d56374ee1ab45f))


## v0.1.4 (2025-05-02)


## v0.1.4-rc.1 (2025-05-02)

### Chores

- **readme**: Fix pypi badge
  ([`bd30d8d`](https://github.com/m-xim/textcompose/commit/bd30d8dee487d5f717cae2275a3687488dfb58b4))


## v0.1.3 (2025-05-02)

### Chores

- **release**: Add project metadata
  ([`727d910`](https://github.com/m-xim/textcompose/commit/727d9109f66f129cccd4a1263036dc8888b376b7))

### Continuous Integration

- Set committer
  ([`d2e1cff`](https://github.com/m-xim/textcompose/commit/d2e1cff651e9fc13a12c6e6cd95584426d4df645))


## v0.1.3-rc.2 (2025-05-02)

### Bug Fixes

- **Container**: `*children`, `when` is name arg
  ([`5d726e5`](https://github.com/m-xim/textcompose/commit/5d726e548691162f38737c4d31903725c63b05d1))

### Continuous Integration

- Cleaning
  ([`17fb568`](https://github.com/m-xim/textcompose/commit/17fb5687113d3f0c3694e963ae153409bc7d4279))

- Fix pip
  ([`71c2d0f`](https://github.com/m-xim/textcompose/commit/71c2d0ffef0e8c85da1c9b89fb6c84568dd81624))

- Fix pytest
  ([`429e0ba`](https://github.com/m-xim/textcompose/commit/429e0ba95c17bc858ab47db9901a75df24ee4b04))

- Fix uv sync
  ([`6152b99`](https://github.com/m-xim/textcompose/commit/6152b99f0155d902096af632a216aed8be8d7d7d))

### Testing

- Add tests
  ([`fa30176`](https://github.com/m-xim/textcompose/commit/fa301760d5734d249c5c7c59a7f9f954de6bf0c4))


## v0.1.3-rc.1 (2025-05-01)

### Bug Fixes

- **Text**: Condition
  ([`1d9dca2`](https://github.com/m-xim/textcompose/commit/1d9dca26f2c2f6c41416c9009a29e3c002feef50))

### Continuous Integration

- Rename
  ([`a3737ed`](https://github.com/m-xim/textcompose/commit/a3737ed9b72de9d9d245bb2398616f9b0822254b))

### Documentation

- Add README
  ([`0ef408e`](https://github.com/m-xim/textcompose/commit/0ef408e808bbde043c5ef12c3928e006b0631183))


## v0.1.2 (2025-05-01)

### Bug Fixes

- Bump version for re-upload
  ([`10e3415`](https://github.com/m-xim/textcompose/commit/10e34150ca94eec75af46fe3bbda121a4b97b802))


## v0.1.1 (2025-05-01)

### Bug Fixes

- Lock
  ([`1811f28`](https://github.com/m-xim/textcompose/commit/1811f28b954106735e1e28d513378a426fb11c15))

- Lock
  ([`6d4b44c`](https://github.com/m-xim/textcompose/commit/6d4b44c8719a45f52834391777d5b98af452a36f))

- Lock
  ([`fbdcd6c`](https://github.com/m-xim/textcompose/commit/fbdcd6caf211c7a6a33ac6acc4a08a2e8bcdeb8f))

- Release.yml
  ([`6a51a9d`](https://github.com/m-xim/textcompose/commit/6a51a9d68cf05e38576de6c29b3244a33fe21a9d))


## v0.1.0 (2025-05-01)

- Initial Release
