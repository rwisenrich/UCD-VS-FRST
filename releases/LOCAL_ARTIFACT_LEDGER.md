# Local artifact integrity ledger

The ChatGPT build environment produced full ZIP deliverables in addition to the source-first GitHub tree. Binary report bundles are retained by SHA-256 even when the GitHub connector cannot directly transfer local binary bytes.

| Release | SHA-256 |
|---|---|
| FRST_UCD_FREEZE_COMPARE_v1_0.zip | `5a75a4795867bd4950383d2a14456098ac5559c81c8f8f4b4af6aaf552401598` |
| FRST_UCD_FREEZE_COMPARE_v1_0_SOURCE_ONLY.zip | `2503fc441692dbbc9586206177af854f22680a073940e98dd338d4bf06d0954e` |
| UCD_VS_FRST_SELECTOR_ACTUALITY_v2_0.zip | `acc7921f50315a59063adb9a0bfd5c2965f1274a9348560f9e1f826ed44e70c5` |
| UCD_VS_FRST_SOURCE_SELECTOR_TOURNAMENT_v3_0.zip | `499bb3314dffa073696ea3eb9e2e7177d1eb25de65ab8cd2204b49715e9bdc0f` |
| UCD_VS_FRST_NATIVE_ACTUALIZATION_GRAMMAR_v4_0.zip | `2b66240013b06cdd427f7c981baaf014dc0ed08a7e5168d9718858be3db95f9f` |
| UCD_VS_FRST_FINITE_SEPARATOR_BASIS_v5_0.zip | `de7afc136d0fc7be133684129fc4cdb7d11134501dd11a094391ce0eabc9b213` |
| UCD_VS_FRST_SOURCE_FINITENESS_ROUTE_AUDIT_v6_0.zip | `29c116e6c24c4339ba3ef0363d22646b08e5b49cc7e667ad66114b0e34201f6d` |

The frozen v1 verdict's historical `github_at_freeze_time=NOT_TOUCHED` records the state at freeze time; later commits to this dedicated repository do not rewrite that historical provenance.