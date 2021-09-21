# This script uses LDLite to extract sample data from folio-snapshot.

import ldlite
ld = ldlite.LDLite()
ld.connect_okapi(url='https://folio-snapshot-okapi.dev.folio.org',
                 tenant='diku',
                 user='diku_admin',
                 password='admin')

db = ld.connect_db(filename='ldlite.db')
# For PostgreSQL, use connect_db_postgresql() instead of connect_db():
# db = ld.connect_db_postgresql(dsn='dbname=ldlite host=localhost user=ldlite')

tables = []
tables += ld.query(table='acquisitions_memberships', path='/acquisitions-units-storage/memberships', query='cql.allRecords=1 sortby id')
tables += ld.query(table='acquisitions_units', path='/acquisitions-units-storage/units', query='cql.allRecords=1 sortby id')
tables += ld.query(table='audit_circulation_logs', path='/audit-data/circulation/logs', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_cancellation_reasons', path='/cancellation-reason-storage/cancellation-reasons', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_check_ins', path='/check-in-storage/check-ins', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_fixed_due_date_schedules', path='/fixed-due-date-schedule-storage/fixed-due-date-schedules', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_loan_history', path='/loan-storage/loan-history', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_loan_policies', path='/loan-policy-storage/loan-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_loans', path='/loan-storage/loans', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_patron_action_sessions', path='/patron-action-session-storage/patron-action-sessions', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_patron_notice_policies', path='/patron-notice-policy-storage/patron-notice-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_request_policies', path='/request-policy-storage/request-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_request_preference', path='/request-preference-storage/request-preference', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_requests', path='/request-storage/requests', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_scheduled_notices', path='/scheduled-notice-storage/scheduled-notices', query='cql.allRecords=1 sortby id')
tables += ld.query(table='circulation_staff_slips', path='/staff-slips-storage/staff-slips', query='cql.allRecords=1 sortby id')
tables += ld.query(table='configuration_entries', path='/configurations/entries', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_copyrightstatuses', path='/coursereserves/copyrightstatuses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_courselistings', path='/coursereserves/courselistings', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_courses', path='/coursereserves/courses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_coursetypes', path='/coursereserves/coursetypes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_departments', path='/coursereserves/departments', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_processingstatuses', path='/coursereserves/processingstatuses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_reserves', path='/coursereserves/reserves', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_roles', path='/coursereserves/roles', query='cql.allRecords=1 sortby id')
tables += ld.query(table='course_terms', path='/coursereserves/terms', query='cql.allRecords=1 sortby id')
tables += ld.query(table='email_email', path='/email', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_accounts', path='/accounts', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_comments', path='/comments', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_feefineactions', path='/feefineactions', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_feefines', path='/feefines', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_lost_item_fees_policies', path='/lost-item-fees-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_manualblocks', path='/manualblocks', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_overdue_fines_policies', path='/overdue-fines-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_owners', path='/owners', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_payments', path='/payments', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_refunds', path='/refunds', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_transfer_criterias', path='/transfer-criterias', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_transfers', path='/transfers', query='cql.allRecords=1 sortby id')
tables += ld.query(table='feesfines_waives', path='/waives', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_budgets', path='/finance-storage/budgets', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_expense_classes', path='/finance-storage/expense-classes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_fiscal_years', path='/finance-storage/fiscal-years', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_fund_types', path='/finance-storage/fund-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_funds', path='/finance-storage/funds', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_group_fund_fiscal_years', path='/finance-storage/group-fund-fiscal-years', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_groups', path='/finance-storage/groups', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_ledgers', path='/finance-storage/ledgers', query='cql.allRecords=1 sortby id')
tables += ld.query(table='finance_transactions', path='/finance-storage/transactions', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_alternative_title_types', path='/alternative-title-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_call_number_types', path='/call-number-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_campuses', path='/location-units/campuses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_classification_types', path='/classification-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_contributor_name_types', path='/contributor-name-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_contributor_types', path='/contributor-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_electronic_access_relationships', path='/electronic-access-relationships', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_holdings', path='/holdings-storage/holdings', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_holdings_note_types', path='/holdings-note-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_holdings_sources', path='/holdings-sources', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_holdings_types', path='/holdings-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_identifier_types', path='/identifier-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_ill_policies', path='/ill-policies', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_formats', path='/instance-formats', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_note_types', path='/instance-note-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_relationship_types', path='/instance-relationship-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_relationships', path='/instance-storage/instance-relationships', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_statuses', path='/instance-statuses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instance_types', path='/instance-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_instances', path='/instance-storage/instances', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_institutions', path='/location-units/institutions', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_item_damaged_statuses', path='/item-damaged-statuses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_item_note_types', path='/item-note-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_items', path='/item-storage/items', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_libraries', path='/location-units/libraries', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_loan_types', path='/loan-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_locations', path='/locations', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_material_types', path='/material-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_modes_of_issuance', path='/modes-of-issuance', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_nature_of_content_terms', path='/nature-of-content-terms', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_service_points', path='/service-points', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_service_points_users', path='/service-points-users', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_statistical_code_types', path='/statistical-code-types', query='cql.allRecords=1 sortby id')
tables += ld.query(table='inventory_statistical_codes', path='/statistical-codes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='invoice_invoices', path='/invoice-storage/invoices', query='cql.allRecords=1 sortby id')
tables += ld.query(table='invoice_lines', path='/invoice-storage/invoice-lines', query='cql.allRecords=1 sortby id')
tables += ld.query(table='invoice_voucher_lines', path='/voucher-storage/voucher-lines', query='cql.allRecords=1 sortby id')
tables += ld.query(table='invoice_vouchers', path='/voucher-storage/vouchers', query='cql.allRecords=1 sortby id')
tables += ld.query(table='notes', path='/notes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_addresses', path='/organizations-storage/addresses', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_categories', path='/organizations-storage/categories', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_contacts', path='/organizations-storage/contacts', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_emails', path='/organizations-storage/emails', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_interfaces', path='/organizations-storage/interfaces', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_organizations', path='/organizations-storage/organizations', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_phone_numbers', path='/organizations-storage/phone-numbers', query='cql.allRecords=1 sortby id')
tables += ld.query(table='organization_urls', path='/organizations-storage/urls', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_alerts', path='/orders-storage/alerts', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_lines', path='/orders-storage/po-lines', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_order_invoice_relns', path='/orders-storage/order-invoice-relns', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_order_templates', path='/orders-storage/order-templates', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_pieces', path='/orders-storage/pieces', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_purchase_orders', path='/orders-storage/purchase-orders', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_receiving_history', path='/orders-storage/receiving-history', query='cql.allRecords=1 sortby id')
tables += ld.query(table='po_reporting_codes', path='/orders-storage/reporting-codes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='user_addresstypes', path='/addresstypes', query='cql.allRecords=1 sortby id')
tables += ld.query(table='user_departments', path='/departments', query='cql.allRecords=1 sortby id')
tables += ld.query(table='user_groups', path='/groups', query='cql.allRecords=1 sortby id')
tables += ld.query(table='user_proxiesfor', path='/proxiesfor', query='cql.allRecords=1 sortby id')
tables += ld.query(table='user_users', path='/users', query='cql.allRecords=1 sortby id')

print('Tables:')
for t in tables:
    print(t)
print('('+str(len(tables))+' tables)')
