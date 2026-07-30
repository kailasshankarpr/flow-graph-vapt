# Flow-Graph VAPT: BOLA Vulnerability Report
**Generated At:** 2026-07-30T16:00:51.022515
**Total Findings:** 738
---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/6
- **Vulnerable Parameter:** `basket_id` (IdentifierLocation.PATH)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `0.85`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `0.85`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `0.85`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/user/whoami
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/user/whoami
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/user/whoami
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/user/whoami
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/6
- **Vulnerable Parameter:** `basket_id` (IdentifierLocation.PATH)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `0.85`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `BasketId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/BasketItems/11
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/BasketItems/11
- **Vulnerable Parameter:** `BasketId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.PUT http://localhost:3000/api/BasketItems/11
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.PUT http://localhost:3000/api/BasketItems/11
- **Vulnerable Parameter:** `BasketId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/6
- **Vulnerable Parameter:** `basket_id` (IdentifierLocation.PATH)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `0.85`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `BasketId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Basket`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `6`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/basket/7
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/products/search?q=
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `11` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `12` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `14` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `15` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `16` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `17` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `20` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `22` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `23` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `24` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `25` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `26` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `27` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `28` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `29` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `30` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `31` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `32` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `33` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `34` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `35` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `36` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `37` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `38` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `39` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `40` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `41` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `42` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `43` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `44` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `45` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `46` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `47` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `48` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `49` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `50` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `51` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `52` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `53` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `54` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `55` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `ProductId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Product`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Quantitys/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `56` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/api/Feedbacks/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernGoogle` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/admin/application-configuration
- **Vulnerable Parameter:** `user` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `bjoernOwasp` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `1` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/13.jpg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `2` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/defaultAdmin.png` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `3` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/defaultAdmin.png` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `4` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `21` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/default.svg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `5` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/13.jpg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `6` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/13.jpg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `7` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/13.jpg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `8` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `13` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/13.jpg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `9` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `18` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/default.svg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `UserId` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `User`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `10` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `9`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `24`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `10`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `id` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `UnknownEntity`
- **Confidence Score:** `1.0`
- **Substitution:** `19` -> `1`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
## [RiskSeverity.HIGH] HTTPMethod.GET http://localhost:3000/rest/memories/
- **Vulnerable Parameter:** `profileImage` (IdentifierLocation.JSON_BODY)
- **Inferred Entity:** `Profileimage`
- **Confidence Score:** `1.0`
- **Substitution:** `assets/public/images/uploads/default.svg` -> `/assets/public/images/uploads/default.svg`
### Remediation Guidance
Implement explicit server-side object-level authorization checks. Ensure the authenticated session principal (user/tenant ID) owns or has explicit permission to access the requested resource ID before returning data from the database.

---
