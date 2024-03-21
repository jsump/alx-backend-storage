-- Create a trigger that decreased the quantity
-- of item after adding a new order
DELIMITER $$
CREATE  TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.quantity
	WHERE items.item_id = NEW.item_id;
END$$
DELIMITER ;
