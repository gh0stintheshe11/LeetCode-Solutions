SELECT
    i.invoice_id,
    c.customer_name,
    i.price,
    IFNULL(cnt.contacts_cnt, 0) AS contacts_cnt,
    IFNULL(tcnt.trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM
    Invoices i
JOIN
    Customers c ON i.user_id = c.customer_id
LEFT JOIN
    (SELECT
        user_id,
        COUNT(*) AS contacts_cnt
     FROM
        Contacts
     GROUP BY
        user_id) cnt ON i.user_id = cnt.user_id
LEFT JOIN
    (SELECT
        con.user_id,
        COUNT(*) AS trusted_contacts_cnt
     FROM
        Contacts con
     JOIN
        Customers cus ON con.contact_email = cus.email
     GROUP BY
        con.user_id) tcnt ON i.user_id = tcnt.user_id
ORDER BY
    i.invoice_id;