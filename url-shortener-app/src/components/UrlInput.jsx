import React, { useEffect } from 'react';

export default function UrlInput({ value, onChange, setIsValidUrl }) {
  useEffect(() => {
    try {
      new URL(value);
      setIsValidUrl(true);
    } catch {
      setIsValidUrl(false);
    }
  }, [value, setIsValidUrl]);

  return (
    <div className="mb-3">
      <label htmlFor="longUrl" className="form-label text-muted">
        Long URL
      </label>
      <input
        type="url"
        id="longUrl"
        className="form-control form-control-lg"
        placeholder="https://your-very-long-url.com/page/123"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        required
      />
    </div>
  );
}
